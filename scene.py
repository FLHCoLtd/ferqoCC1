
from homeassistant.helpers.entity import Entity
import logging
from .const import DOMAIN

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Add the Sonoff Sensor entities"""


    # for device in hass.data[DOMAIN].get_devices(force_update = False):
        # as far as i know only 1-switch devices seem to have sensor-like capabilities
    async def loadingentities():
        entities = []
        for device in hass.data[DOMAIN].getEntitiesType("s"):
            CC_device = FerqoCCSensor(device, hass)
            entities.append(CC_device)
        return entities
    entities = await loadingentities()
    if len(entities):
        async_add_entities(entities, update_before_add=False)
        return True

class FerqoCCSensor(Entity):
    """Representation of a sensor."""
    def __init__(self, CC_device, hass):
        self.hub = hass.data[DOMAIN]
        self.CC_device = CC_device
        self.sensorType = CC_device["sensorType"]
        self._state = CC_device[str(CC_device["sensorType"])]
        self.unit = CC_device["sensorUnit"]
        self._name = "Ferqo." + CC_device["name"]
        self.node_id = CC_device["node_id"]

    @property
    def name(self):
        """Return the name of the device."""
        return self._name
    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement."""
        return self.unit

    async def async_update(self):
        """Retrieve latest state."""
        List = self.hub.getEntitiesType("sensor")
        self.CC_List = List
        for i in range(len(self.CC_List)):
            if (self.node_id == self.CC_List[i]["node_id"]):
                if (self.sensorType == self.CC_List[i]["sensorType"]):
                    self._state = self.CC_List[i][str(self.CC_List[i]["sensorType"])]
                    self._name = "Ferqo." + self.CC_List[i]["name"]
