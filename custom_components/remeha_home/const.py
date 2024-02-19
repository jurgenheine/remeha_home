"""Constants for the Remeha Home integration."""
from homeassistant.components.sensor import (
    SensorEntityDescription,
    SensorDeviceClass,
    SensorStateClass,
)
from homeassistant.components.binary_sensor import (
    BinarySensorEntityDescription,
    BinarySensorDeviceClass,
)
from homeassistant.const import UnitOfEnergy, UnitOfTemperature, UnitOfPressure

DOMAIN = "remeha_home"

APPLIANCE_SENSOR_TYPES = [
    SensorEntityDescription(
        key="waterPressure",
        name="Water Pressure",
        native_unit_of_measurement=UnitOfPressure.BAR,
        device_class=SensorDeviceClass.PRESSURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="outdoorTemperature",
        name="Outdoor Temperature",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="outdoorTemperatureInformation.cloudOutdoorTemperature",
        name="Cloud Outdoor Temperature",
        entity_registry_enabled_default=False,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="consumptionData.heatingEnergyConsumed",
        name="Today heating Energy Consumed",
        entity_registry_enabled_default=False,
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key="consumptionData.hotWaterEnergyConsumed",
        name="Today hot Water Energy Consumed",
        entity_registry_enabled_default=False,
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key="consumptionData.coolingEnergyConsumed",
        name="Today cooling Energy Consumed",
        entity_registry_enabled_default=False,
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key="consumptionData.heatingEnergyDelivered",
        name="Today heating Energy Delivered",
        entity_registry_enabled_default=False,
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key="consumptionData.hotWaterEnergyDelivered",
        name="Today hot Water Energy Delivered",
        entity_registry_enabled_default=False,
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key="consumptionData.coolingEnergyDelivered",
        name="Today cooling Energy Delivered",
        entity_registry_enabled_default=False,
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key="consumptionData.heatingCOP",
        name="Today heating COP",
        entity_registry_enabled_default=False
    ),
    SensorEntityDescription(
        key="consumptionData.coolingCOP",
        name="Today cooling COP",
        entity_registry_enabled_default=False
    ),
    SensorEntityDescription(
        key="consumptionData.hotWaterCOP",
        name="Today hot water COP",
        entity_registry_enabled_default=False
    ),
    SensorEntityDescription(
        key="increaseConsumptionData.heatingEnergyConsumed",
        name="Current heating Energy Consumed",
        entity_registry_enabled_default=False,
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key="increaseConsumptionData.hotWaterEnergyConsumed",
        name="Current hot Water Energy Consumed",
        entity_registry_enabled_default=False,
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key="increaseConsumptionData.coolingEnergyConsumed",
        name="Current cooling Energy Consumed",
        entity_registry_enabled_default=False,
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key="increaseConsumptionData.heatingEnergyDelivered",
        name="Current heating Energy Delivered",
        entity_registry_enabled_default=False,
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key="increaseConsumptionData.hotWaterEnergyDelivered",
        name="Current hot Water Energy Delivered",
        entity_registry_enabled_default=False,
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key="increaseConsumptionData.coolingEnergyDelivered",
        name="Current cooling Energy Delivered",
        entity_registry_enabled_default=False,
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key="increaseConsumptionData.heatingCOP",
        name="Current heating COP",
        entity_registry_enabled_default=False
    ),
    SensorEntityDescription(
        key="increaseConsumptionData.coolingCOP",
        name="Current cooling COP",
        entity_registry_enabled_default=False
    ),
    SensorEntityDescription(
        key="increaseConsumptionData.hotWaterCOP",
        name="Current hot water COP",
        entity_registry_enabled_default=False
    ),
    SensorEntityDescription(
        key="totalConsumptionData.heatingEnergyConsumed",
        name="Total heating Energy Consumed",
        entity_registry_enabled_default=False,
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key="totalConsumptionData.hotWaterEnergyConsumed",
        name="Total hot Water Energy Consumed",
        entity_registry_enabled_default=False,
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key="totalConsumptionData.coolingEnergyConsumed",
        name="Total cooling Energy Consumed",
        entity_registry_enabled_default=False,
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key="totalConsumptionData.heatingEnergyDelivered",
        name="Total heating Energy Delivered",
        entity_registry_enabled_default=False,
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key="totalConsumptionData.hotWaterEnergyDelivered",
        name="Total hot Water Energy Delivered",
        entity_registry_enabled_default=False,
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key="totalConsumptionData.coolingEnergyDelivered",
        name="Total cooling Energy Delivered",
        entity_registry_enabled_default=False,
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key="totalConsumptionData.heatingCOP",
        name="Total heating COP",
        entity_registry_enabled_default=False
    ),
    SensorEntityDescription(
        key="totalConsumptionData.coolingCOP",
        name="Total cooling COP",
        entity_registry_enabled_default=False
    ),
    SensorEntityDescription(
        key="totalConsumptionData.hotWaterCOP",
        name="Total hot water COP",
        entity_registry_enabled_default=False
    ),
    SensorEntityDescription(
        key="yearlyConsumptionData.heatingEnergyConsumed",
        name="Current year heating Energy Consumed",
        entity_registry_enabled_default=False,
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key="yearlyConsumptionData.hotWaterEnergyConsumed",
        name="Current year hot Water Energy Consumed",
        entity_registry_enabled_default=False,
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key="yearlyConsumptionData.coolingEnergyConsumed",
        name="Current year cooling Energy Consumed",
        entity_registry_enabled_default=False,
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key="yearlyConsumptionData.heatingEnergyDelivered",
        name="Current year heating Energy Delivered",
        entity_registry_enabled_default=False,
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key="yearlyConsumptionData.hotWaterEnergyDelivered",
        name="Current year hot Water Energy Delivered",
        entity_registry_enabled_default=False,
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key="yearlyConsumptionData.coolingEnergyDelivered",
        name="Current year cooling Energy Delivered",
        entity_registry_enabled_default=False,
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key="yearlyConsumptionData.heatingCOP",
        name="Current year heating COP",
        entity_registry_enabled_default=False
    ),
    SensorEntityDescription(
        key="yearlyConsumptionData.coolingCOP",
        name="Current year cooling COP",
        entity_registry_enabled_default=False
    ),
    SensorEntityDescription(
        key="yearlyConsumptionData.hotWaterCOP",
        name="Current year hot water COP",
        entity_registry_enabled_default=False
    ),
    SensorEntityDescription(
        key="monthlyConsumptionData.heatingEnergyConsumed",
        name="Current month heating Energy Consumed",
        entity_registry_enabled_default=False,
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key="monthlyConsumptionData.hotWaterEnergyConsumed",
        name="Current month hot Water Energy Consumed",
        entity_registry_enabled_default=False,
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key="monthlyConsumptionData.coolingEnergyConsumed",
        name="Current month cooling Energy Consumed",
        entity_registry_enabled_default=False,
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key="monthlyConsumptionData.heatingEnergyDelivered",
        name="Current month heating Energy Delivered",
        entity_registry_enabled_default=False,
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key="monthlyConsumptionData.hotWaterEnergyDelivered",
        name="Current month hot Water Energy Delivered",
        entity_registry_enabled_default=False,
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key="monthlyConsumptionData.coolingEnergyDelivered",
        name="Current month cooling Energy Delivered",
        entity_registry_enabled_default=False,
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key="monthlyConsumptionData.heatingCOP",
        name="Current month heating COP",
        entity_registry_enabled_default=False
    ),
    SensorEntityDescription(
        key="monthlyConsumptionData.coolingCOP",
        name="Current month cooling COP",
        entity_registry_enabled_default=False
    ),
    SensorEntityDescription(
        key="monthlyConsumptionData.hotWaterCOP",
        name="Current month hot water COP",
        entity_registry_enabled_default=False
    )
]

CLIMATE_ZONE_SENSOR_TYPES = [
    SensorEntityDescription(
        key="nextSetpoint",
        name="Next Setpoint",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
    ),
    SensorEntityDescription(
        key="nextSwitchTime",
        name="Next Setpoint Time",
        device_class=SensorDeviceClass.TIMESTAMP,
    ),
    SensorEntityDescription(
        key="currentScheduleSetPoint",
        name="Current Schedule Setpoint",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
    ),
]

HOT_WATER_ZONE_SENSOR_TYPES = [
    SensorEntityDescription(
        key="dhwTemperature",
        name="Water Temperature",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="dhwStatus",
        name="Status",
        entity_registry_enabled_default=False,
    ),
]

CLIMATE_ZONE_BINARY_SENSOR_TYPES = [
    (
        BinarySensorEntityDescription(
            key="activeComfortDemand",
            name="Status",
            entity_registry_enabled_default=False,
            device_class=BinarySensorDeviceClass.HEAT,
        ),
        lambda value: value in ["ProducingHeat", "RequestingHeat"],
    )
]

HOT_WATER_ZONE_BINARY_SENSOR_TYPES = [
    (
        BinarySensorEntityDescription(
            key="dhwStatus",
            name="Status",
            entity_registry_enabled_default=False,
            device_class=BinarySensorDeviceClass.HEAT,
        ),
        lambda value: value == "ProducingHeat",
    ),
]
