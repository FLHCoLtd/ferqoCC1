from .FerqoCCApi.apiDataFormat.device import deviceExecute
from .FerqoCCApi.service.cloud import sendHttp
from homeassistant.components.switch import SwitchEntity

import logging
from .const import DOMAIN

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Add the Sonoff Sensor entities"""

    # for device in hass.data[DOMAIN].get_devices(force_update = False):
        # as far as i know only 1-switch devices seem to have sensor-like capabilities
    async def loadingentities():
        entities = []
        for device in hass.data[DOMAIN].getEntitiesType("switch"):
            CC_device = FerqoCCSwitch(hass,device)
            entities.append(CC_device)
        return entities
    entities = await loadingentities()
    if len(entities):
        async_add_entities(entities, update_before_add=False)
        return True

class FerqoCCSwitch(SwitchEntity):
    """Representation of a sensor."""
    def __init__(self, hass, CC_device):
        self.hub = hass.data[DOMAIN]
        self.gatewayAuth = hass.data[DOMAIN].gatewayAuth
        self._name = "Ferqo." + CC_device["name"]
        state = CC_device["status"]
        if (state == "ON"):
            self._state = True
        elif (state == "OFF"):
            self._state = False
        self.node_id = CC_device["node_id"]
        self.CC_device = CC_device

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def is_on(self):
        """Return true if device is on."""
        return self._state

    def turn_on(self, **kwargs):
        """Instruct the light to turn on.

        You can skip the brightness part if your light does not support
        brightness control.
        """
        cmd = deviceExecute(self.gatewayAuth)
        cmd.setNodeid(self.node_id)
        cmd.switchAction("turnOn")
        sendHttp(cmd.body)
        self._state = True
        # self.update_Hub
    def turn_off(self, **kwargs):
        """Instruct the light to turn off."""
        cmd = deviceExecute(self.gatewayAuth)
        cmd.setNodeid(self.node_id)
        cmd.switchAction("turnOff")
        sendHttp(cmd.body)
        self._state = False
        # self.update_Hub
    @property
    def current_power_w(self):
        """Return the current power usage in W."""
        if "powerNow" in self.CC_device:
            self.powerNow = self.CC_device["powerNow"]
        else:
            self.powerNow = None
        return self.powerNow

    @property
    def today_energy_kwh(self):
        """Return the today total energy usage in kWh."""
        if "powerTotal" in self.CC_device:
            self.powerTotal = self.CC_device["powerTotal"]
        else:
            self.powerTotal = None
        return self.powerTotal

    async def async_update(self):
        """Retrieve latest state."""
        List = self.hub.getEntitiesType("switch")
        self.CC_List = List
        for i in range(len(self.CC_List)):
            if (self.node_id == self.CC_List[i]["node_id"]):
                self._name = "Ferqo." + self.CC_List[i]["name"]
                state = self.CC_List[i]["status"]
                if (state == "ON"):
                    self._state = True
                elif (state == "OFF"):
                    self._state = False
    def update_Hub(self):
        self.hub.getEntitiesList()
