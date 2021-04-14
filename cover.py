from .FerqoCCApi.apiDataFormat.device import deviceExecute
from .FerqoCCApi.service.cloud import sendHttp



import logging

from homeassistant.components.cover import CoverEntity

from .const import DOMAIN

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Add the Sonoff Sensor entities"""

    async def loadingentities():
        entities = []
        for device in hass.data[DOMAIN].getEntitiesType("cover"):
            CC_device = FerqoCCCover(hass, device)
            entities.append(CC_device)
        return entities

    entities = await loadingentities()
    if len(entities):
        async_add_entities(entities, update_before_add=False)
        return True

class FerqoCCCover(CoverEntity):
    """Representation of a sensor."""
    def __init__(self, hass, CC_device):
        self.hub = hass.data[DOMAIN]
        self.gatewayAuth = hass.data[DOMAIN].gatewayAuth
        self.node_id = CC_device["node_id"]
        self.CC_device = CC_device
        self._name = "Ferqo." + CC_device["name"]
        state = CC_device["status"]
        if (state == "Open"):
            self._state = 0
        elif (state == "Close"):
            self._state = 100
    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def current_cover_position(self):
        """Return current position of cover.
        None is unknown, 0 is closed, 100 is fully open.
        """
        return self._state
    @property
    def is_closed(self):
        if self.current_cover_position is not None:
            return self.current_cover_position == 0

    def open_cover(self, **kwargs):
        """Open the cover."""
        cmd = deviceExecute(self.gatewayAuth)
        cmd.setNodeid(self.node_id)
        cmd.BlindsAction("open")
        sendHttp(cmd.body)
        print(cmd.body)
        self._state = 100
        # self.update_Hub
    def close_cover(self, **kwargs):
        """Close the cover."""
        cmd = deviceExecute(self.gatewayAuth)
        cmd.setNodeid(self.node_id)
        cmd.BlindsAction("close")
        sendHttp(cmd.body)
        self._state = 0
        # self.update_Hub
    def stop_cover(self, **kwargs):
        """Stop the cover."""
        cmd = deviceExecute(self.gatewayAuth)
        cmd.setNodeid(self.node_id)
        cmd.BlindsAction("stop")
        sendHttp(cmd.body)
        self._state = 50
        # self.update_Hub
    async def async_update(self):
        """Retrieve latest state."""
        List = self.hub.getEntitiesType("cover")
        self.CC_List = List
        for i in range(len(self.CC_List)):
            if (self.node_id == self.CC_List[i]["node_id"]):
                self._name = "Ferqo." + self.CC_List[i]["name"]
                state = self.CC_List[i]["status"]
                if (state == "Open"):
                    self._state = 0
                elif (state == "Close"):
                    self._state = 100
    def update_Hub(self):
        self.hub.getEntitiesList()