"""Coordinator for fetching the Remeha Home data."""
from datetime import datetime, timedelta
import logging

import async_timeout
from aiohttp.client_exceptions import ClientResponseError

from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.typing import HomeAssistantType
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from homeassistant.exceptions import ConfigEntryAuthFailed

from .api import RemehaHomeAPI
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)


class RemehaHomeUpdateCoordinator(DataUpdateCoordinator):
    """Remeha Home update coordinator."""

    def __init__(self, hass: HomeAssistantType, api: RemehaHomeAPI) -> None:
        """Initialize Remeha Home update coordinator."""
        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=timedelta(seconds=60),
        )
        self.api = api
        self.items = {}
        self.device_info = {}
        self.technical_info = {}
        self.appliance_consumption_data = {}
        self.appliance_increase_consumption_data = {}
        self.appliance_total_consumption_data = {}
        self.appliance_thismonth_consumption_data = {}
        self.appliance_thisyear_consumption_data = {}
        self.appliance_last_consumption_data_update = {}
        self.appliance_last_consumption_data_dayly_update = {}

    async def _async_update_data(self):
        """Fetch data from API endpoint.

        This is the place to pre-process the data to lookup tables
        so entities can quickly look up their data.
        """
        data = await self.async_get_dashboard_data()

        # Save the current time for appliance usage data updates
        now = datetime.now()

        for appliance in data["appliances"]:
            appliance_id = appliance["applianceId"]
            self.items[appliance_id] = appliance

            await self.async_update_technical_data(appliance_id)
            await self.async_update_power_consumption(appliance_id, now, appliance)
            self.update_device_info(appliance_id, appliance)
            self.update_climate_zones(appliance_id, appliance)
            self.update_hot_water_zones(appliance_id, appliance)

        return data

    def get_by_id(self, item_id: str):
        """Return item with the specified item id."""
        return self.items.get(item_id)

    def get_device_info(self, item_id: str):
        """Return device info for the item with the specified id."""
        return self.device_info.get(item_id)

    async def async_get_dashboard_data(self):
        """Return current dashboard data."""
        try:
            # Note: asyncio.TimeoutError and aiohttp.ClientError are already
            # handled by the data update coordinator.
            async with async_timeout.timeout(30):
                return await self.api.async_get_dashboard()
        except ClientResponseError as err:
            # Raising ConfigEntryAuthFailed will cancel future updates
            # and start a config flow with SOURCE_REAUTH (async_step_reauth)
            if err.status == 401:
                raise ConfigEntryAuthFailed from err

            raise UpdateFailed from err

    async def async_update_technical_data(self, appliance_id):
        """Update technical data."""
        # Request appliance technical information the first time it is discovered
        if appliance_id not in self.technical_info:
            self.technical_info[
                appliance_id
            ] = await self.api.async_get_appliance_technical_information(
                appliance_id
            )
            _LOGGER.debug(
                "Requested technical information for appliance %s: %s",
                appliance_id,
                self.technical_info[appliance_id],
            )

    def update_device_info(self, appliance_id, appliance):
        """Update device info."""
        self.device_info[appliance_id] = DeviceInfo(
            identifiers={(DOMAIN, appliance_id)},
            name=appliance["houseName"],
            manufacturer="Remeha",
            model=self.technical_info[appliance_id]["applianceName"],
        )

    def update_climate_zones(self, appliance_id, appliance):
        """Update climate zones."""
        for climate_zone in appliance["climateZones"]:
            climate_zone_id = climate_zone["climateZoneId"]
            # This assumes that all climate zones for an appliance share the same gateway
            gateways = self.technical_info[appliance_id][
                "internetConnectedGateways"
            ]

            if len(gateways) > 1:
                _LOGGER.warning(
        "Appliance %s has more than one gateway, using technical information from the first one",
                    appliance_id,
                )

            if len(gateways) > 0:
                gateway_info = gateways[0]
            else:
                _LOGGER.warning(
                    "Appliance %s has no gateways, using unknown values",
                    appliance_id,
                )
                gateway_info = {
                    "name": "Unknown",
                    "hardwareVersion": "Unknown",
                    "softwareVersion": "Unknown",
                }

            self.items[climate_zone_id] = climate_zone
            self.device_info[climate_zone_id] = DeviceInfo(
                identifiers={(DOMAIN, climate_zone_id)},
                name=climate_zone["name"],
                manufacturer="Remeha",
                model=gateway_info["name"],
                hw_version=gateway_info["hardwareVersion"],
                sw_version=gateway_info["softwareVersion"],
                via_device=(DOMAIN, appliance_id),
            )

    def update_hot_water_zones(self, appliance_id, appliance):
        """Update hotwater zones."""
        for hot_water_zone in appliance["hotWaterZones"]:
            hot_water_zone_id = hot_water_zone["hotWaterZoneId"]
            self.items[hot_water_zone_id] = hot_water_zone
            self.device_info[hot_water_zone_id] = DeviceInfo(
                identifiers={(DOMAIN, hot_water_zone_id)},
                name=hot_water_zone["name"],
                manufacturer="Remeha",
                model="Hot Water Zone",
                via_device=(DOMAIN, appliance_id),
            )

    async def async_update_power_consumption(self, appliance_id, now, appliance):
        """Update power consumption."""
        await self.async_get_power_consumptions(appliance_id, now)

        await self.async_update_power_consumption_today(appliance_id, appliance)
        await self.async_update_power_consumption_total(appliance_id, appliance)
        await self.async_update_power_consumption_yearly(appliance_id, appliance)
        await self.async_update_power_consumption_monthly(appliance_id, appliance)

    async def async_get_power_consumptions(self,appliance_id, now):
        """Get power consumptions."""
        self.init_power_consumptions(appliance_id)
        await self.async_get_totals_power_consumption( appliance_id, now)
        await self.async_get_power_consumption_today( appliance_id, now)

    def init_power_consumptions(self, appliance_id):
        """Initialize power consumption data to empty when not yet set."""

        if appliance_id not in self.appliance_consumption_data:
            self.appliance_consumption_data[appliance_id] = self.get_empty_power_values()

        if appliance_id not in self.appliance_increase_consumption_data:
            self.appliance_increase_consumption_data[appliance_id] = self.get_empty_power_values()

        if appliance_id not in self.appliance_total_consumption_data:
            self.appliance_total_consumption_data[
                        appliance_id
                    ] =self.get_empty_power_values()

        if appliance_id not in self.appliance_thisyear_consumption_data:
            self.appliance_thisyear_consumption_data[
                        appliance_id
                ] =self.get_empty_power_values()

        if appliance_id not in self.appliance_thismonth_consumption_data:
            self.appliance_thismonth_consumption_data[
                        appliance_id
                    ] =self.get_empty_power_values()

    async def async_get_power_consumption_today(self, appliance_id, now):
        """Update current day power consumption data."""

        # Only update appliance usage data every 15 minutes
        if (( appliance_id not in self.appliance_last_consumption_data_update)
              or ( now - self.appliance_last_consumption_data_update[appliance_id]
                   >= timedelta(minutes=14, seconds=45))):
            try:
                consumption_data = (await
                                    self.api.async_get_consumption_data_for_today( appliance_id )
                                    or self.get_empty_power_values())

                _LOGGER.debug(
                    "Requested consumption data for appliance %s: %s",
                    appliance_id,
                    consumption_data
                )

                # We need to set increae values directly because we need last result
                self.appliance_increase_consumption_data = self.diff_power_results(
                        consumption_data,
                        self.appliance_consumption_data[
                            appliance_id
                        ])

                self.appliance_consumption_data[ appliance_id
                        ] = self.calculate_cop( consumption_data)

                self.appliance_last_consumption_data_update[appliance_id] = now
            except ClientResponseError as err:
                _LOGGER.warning(
                    "Failed to request consumption data for appliance %s: %s",
                    appliance_id,
                    err,
                )

    async def async_update_power_consumption_today(self, appliance_id, appliance):
        """Update current day power consumption data."""

        # Get the cached consumption data for the appliance or use default values
        appliance[appliance_id]["consumptionData"] = self.appliance_consumption_data[
                appliance_id
            ]

        appliance[appliance_id]["increaseConsumptionData"] = (
                self.appliance_increase_consumption_data[
                appliance_id
                ])

    async def async_get_totals_power_consumption(self, appliance_id, now):
        """Get power consumption data."""

        if ( appliance_id not in self.appliance_last_consumption_data_dayly_update
             or now.date() >
             self.appliance_last_consumption_data_dayly_update[appliance_id].date()):
            try:
                self.appliance_total_consumption_data[
                        appliance_id
                    ]  = (await
                    self.api.async_get_total_consumption_data_till_today( appliance_id ))
                self.appliance_thisyear_consumption_data[
                        appliance_id
                    ]  = (await
                    self.api.async_get_current_year_consumption_data_till_today( appliance_id ))
                self.appliance_thismonth_consumption_data[
                        appliance_id
                    ]  = (await
                    self.api.async_get_current_month_consumption_data_till_today( appliance_id ))

                self.appliance_last_consumption_data_dayly_update[appliance_id] = now
            except ClientResponseError as err:
                _LOGGER.warning(
                    "Failed to request consumption data for appliance %s: %s",
                    appliance_id,
                    err,
                )

    async def async_update_power_consumption_total(self, appliance_id, appliance):
        """Update total power consumption data."""

        # Get the cached total and current dayconsumption data for the appliance
        appliance[appliance_id]["totalConsumptionData"] = self.sum_power_results(
            self.appliance_total_consumption_data[
                appliance_id
            ],
            self.appliance_consumption_data[
                appliance_id
            ]
        )

    async def async_update_power_consumption_yearly(self, appliance_id, appliance):
        """Update yearly power consumption data."""

        # Get the cached total and current dayconsumption data for the appliance
        appliance[appliance_id]["yearlyConsumptionData"] = self.sum_power_results(
            self.appliance_thisyear_consumption_data[
                appliance_id
            ],
            self.appliance_consumption_data[
                appliance_id
            ]
        )

    async def async_update_power_consumption_monthly(self, appliance_id, appliance):
        """Update yearly power consumption data."""

        # Get the cached total and current dayconsumption data for the appliance
        appliance[appliance_id]["monthlyConsumptionData"] = self.sum_power_results(
            self.appliance_thismonth_consumption_data[
                appliance_id
            ],
            self.appliance_consumption_data[
                appliance_id
            ]
        )

    def sum_power_results(self, power_response1, power_response2):
        """Return Sum of both power results."""

        heating_energy_consumed = (power_response1["heatingEnergyConsumed"] +
                                   power_response2["heatingEnergyConsumed"])
        hot_water_energy_consumed = (power_response1["hotWaterEnergyConsumed"] +
                                     power_response2["hotWaterEnergyConsumed"])
        cooling_energy_consumed = (power_response1["coolingEnergyConsumed"] +
                                   power_response2["coolingEnergyConsumed"])
        heating_energy_delivered = (power_response1["heatingEnergyDelivered"] +
                                    power_response2["heatingEnergyDelivered"])
        hot_water_energy_delivered = (power_response1["hotWaterEnergyDelivered"] +
                                      power_response2["hotWaterEnergyDelivered"])
        cooling_energy_delivered = (power_response1["coolingEnergyDelivered"] +
                                    power_response2["coolingEnergyDelivered"])
        return self.calculate_cop({"heatingEnergyConsumed": heating_energy_consumed,
            "hotWaterEnergyConsumed": hot_water_energy_consumed,
            "coolingEnergyConsumed": cooling_energy_consumed,
            "heatingEnergyDelivered": heating_energy_delivered,
            "hotWaterEnergyDelivered": hot_water_energy_delivered,
            "coolingEnergyDelivered": cooling_energy_delivered})

    def diff_power_results(self, power_response1, power_response2):
        """Return diff between the power results."""

        heating_energy_consumed = abs(power_response1["heatingEnergyConsumed"] -
                                   power_response2["heatingEnergyConsumed"])
        hot_water_energy_consumed = abs(power_response1["hotWaterEnergyConsumed"] -
                                     power_response2["hotWaterEnergyConsumed"])
        cooling_energy_consumed = abs(power_response1["coolingEnergyConsumed"] -
                                   power_response2["coolingEnergyConsumed"])
        heating_energy_delivered = abs(power_response1["heatingEnergyDelivered"] -
                                    power_response2["heatingEnergyDelivered"])
        hot_water_energy_delivered = abs(power_response1["hotWaterEnergyDelivered"] -
                                      power_response2["hotWaterEnergyDelivered"])
        cooling_energy_delivered = abs(power_response1["coolingEnergyDelivered"] -
                                    power_response2["coolingEnergyDelivered"])
        return self.calculate_cop({"heatingEnergyConsumed": heating_energy_consumed,
            "hotWaterEnergyConsumed": hot_water_energy_consumed,
            "coolingEnergyConsumed": cooling_energy_consumed,
            "heatingEnergyDelivered": heating_energy_delivered,
            "hotWaterEnergyDelivered": hot_water_energy_delivered,
            "coolingEnergyDelivered": cooling_energy_delivered})

    def calculate_cop(self, power_response):
        """Calculate and add cop values."""
        power_response["heatingCOP"] = float('Inf')
        power_response["coolingCOP"] = float('Inf')
        power_response["hotWaterCOP"] = float('Inf')

        if power_response["heatingEnergyConsumed"] != 0.0:
            power_response["heatingCOP"] = (power_response["heatingEnergyDelivered"]  /
                                            power_response["heatingEnergyConsumed"])
        if power_response["coolingEnergyConsumed"] != 0.0:
            power_response["coolingCOP"] = (power_response["coolingEnergyDelivered"]  /
                                            power_response["coolingEnergyConsumed"])
        if power_response["hotWaterEnergyConsumed"] != 0.0:
            power_response["hotWaterCOP"] = (power_response["hotWaterEnergyDelivered"]  /
                                             power_response["hotWaterEnergyConsumed"])

        return  power_response

    def get_empty_power_values(self):
        """Get empty power values"""
        return  {
            "heatingEnergyConsumed": 0.0,
            "hotWaterEnergyConsumed": 0.0,
            "coolingEnergyConsumed": 0.0,
            "heatingEnergyDelivered": 0.0,
            "hotWaterEnergyDelivered": 0.0,
            "coolingEnergyDelivered": 0.0,
            "heatingCOP" : float('Inf'),
            "coolingCOP" : float('Inf'),
            "hotWaterCOP" : float('Inf')
        }
