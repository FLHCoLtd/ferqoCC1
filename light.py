from .FerqoCCApi.apiDataFormat.device import deviceExecute
from .FerqoCCApi.service.cloud import sendHttp
import asyncio
from homeassistant.components.light import (
    ATTR_BRIGHTNESS,
    ATTR_HS_COLOR,
    ATTR_WHITE_VALUE,
    DOMAIN,
    SUPPORT_BRIGHTNESS,
    SUPPORT_COLOR,
    SUPPORT_WHITE_VALUE,
    LightEntity,
)
import logging
from .const import DOMAIN
from functools import partial
def setup_platform(hass, config,add_entities, discovery_info=None):
    """Add the Sonoff Sensor entities"""

    def loadingentities():
        entities = []
        for device in hass.data[DOMAIN].getEntitiesType("light"):
            CC_device = FerqoCCLight(hass, device)
            entities.append(CC_device)
        return entities

    entities = loadingentities()
    if len(entities):
        add_entities(entities, update_before_add=False)
        return True

class FerqoCCLight(LightEntity):
    """Representation of a sensor."""
    def __init__(self, hass, CC_device):
        self.hub = hass.data[DOMAIN]
        # self._supported_flags = 0
        self.gatewayAuth = hass.data[DOMAIN].gatewayAuth
        self.node_id = CC_device["node_id"]
        self.CC_device = CC_device
        self.subType = CC_device["subType"]
        if "channelName" in CC_device:
            self.channel = CC_device["channelName"]
            self._name = "Ferqo." + CC_device["name"] + CC_device["channelName"]
        else:
            self._name = "Ferqo." + CC_device["name"]
        self._brightness = None
        if "subType" in CC_device:
            if (self.CC_device["subType"] == "multilevel"):
                # self._supported_flags |= SUPPORT_BRIGHTNESS
                self._brightness = int(CC_device["brightness"])
        else:
            pass
        self.signal = None
        if "signal" in CC_device:
            self.signal = CC_device["signal"]
        else:
            pass
        state = CC_device["status"]
        if (state == "ON"):
            self._state = True
        elif (state == "OFF"):
            self._state = False
    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def brightness(self):
        """Return the brightness of the light."""
        return self.brightness

    @property
    def is_on(self):
        """Return true if device is on."""
        return self._state


    def turn_on(self, **kwargs):
        """Instruct the light to turn on.

        You can skip the brightness part if your light does not support
        brightness control.
        """
        self._state = True
        cmd = deviceExecute(self.gatewayAuth)
        cmd.setNodeid(self.node_id)
        if (self.subType == "multilevel"):
            cmd.MultilevelAction("turnOn")
        elif (self.signal == "output"):
            cmd.multiChannelAction(self.channel,"turnOn")
        elif (self.subType == "switch"):
            cmd.switchAction("turnOn")
        sendHttp(cmd.body)

    def turn_off(self, **kwargs):
        """Instruct the light to turn off."""
        self._state = False
        cmd = deviceExecute(self.gatewayAuth)
        cmd.setNodeid(self.node_id)
        if (self.subType == "multilevel"):
            cmd.MultilevelAction("turnOff")
        elif (self.signal == "output"):
            cmd.multiChannelAction(self.channel,"turnOff")
        elif (self.subType == "switch"):
            cmd.switchAction("turnOff")
        sendHttp(cmd.body)

    # def supported_features(self):
    #     """Flag supported features."""
    #     return self._supported_flags

    # def state_attributes(self):
    #     """Return state attributes."""
    #     if not self.is_on:
    #         return None
    #
    #     data = {}
    #     supported_features = self._supported_flags
    #
    #     if supported_features & SUPPORT_BRIGHTNESS:
    #         data[ATTR_BRIGHTNESS] = self.brightness


    def update(self):
        """Retrieve latest state."""
        List = self.hub.getEntitiesType("light")
        self.CC_List = List
        for i in range(len(self.CC_List)):
            if (self.node_id == self.CC_List[i]["node_id"]):
                if "channelName" in self.CC_List[i]:
                    if (self._name == "Ferqo." + self.CC_List[i]["name"] + self.CC_List[i]["channelName"]):
                        state = self.CC_List[i]["status"]
                        if (state == "ON"):
                            self._state = True
                        elif (state == "OFF"):
                            self._state = False
                elif (self._name == "Ferqo." + self.CC_List[i]["name"]):
                    state = self.CC_List[i]["status"]
                    if (state == "ON"):
                        self._state = True
                    elif (state == "OFF"):
                        self._state = False
    # def update_Hub(self):
    #     self.hub.getEntitiesList()
    #     self.async_update()