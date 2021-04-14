from .FerqoCCApi.apiDataFormat.device import device
from .FerqoCCApi.apiDataFormat.scene import scene
from .FerqoCCApi.service.HAType import HAType, MutichannelValueSplit, SensorValueSplit
from .FerqoCCApi.service.cloud import sendHttp
from .FerqoCCApi.service.httpResPhasing import dataAnalytics, sceneAnalytics
from .const import DOMAIN

from homeassistant.const import (
    CONF_HOST,
    CONF_USERNAME,
    CONF_PASSWORD,

)
class FerqoCCApi:
    """Example config flow."""

    def __init__(self, config):
        self.gatewayAuth = {}
        self.gatewayAuth["gateway_id"] = config[DOMAIN][CONF_HOST]
        self.gatewayAuth["account"] = config[DOMAIN][CONF_USERNAME]
        self.gatewayAuth["password"] = config[DOMAIN][CONF_PASSWORD]
    def device_request_body(self):
        self.device_query_cmd = device(self.gatewayAuth)
        return self.device_query_cmd.body
    def scene_request_body(self):
        self.scene_query_cmd = scene(self.gatewayAuth)
        return self.scene_query_cmd.boy
    def getDeviceList(self):
        self.deviceList = HAType(dataAnalytics(sendHttp(self.device_request_body())))
        return self.deviceList
    def getSceneList(self):
        self.sceneList = sceneAnalytics(sendHttp(self.scene_request_body()))
        return self.sceneList
    def listToHAType(self):
        self.deviceList = self.getDeviceList()
        self.deviceList["sensor"] = SensorValueSplit(self.deviceList["sensor"])
        self.deviceList["light"] = MutichannelValueSplit(self.deviceList["light"])
        return self.deviceList
    def getEntitiesList(self):
        self.deviceList = self.listToHAType()
        return self.deviceList
    def getEntitiesType(self,component):
        return self.deviceList[str(component)]
    async def fetch_data(self):
        self.getEntitiesList()
        return self.deviceList
    def get_devices(self, force_update = False):
        if force_update:
            return self.fetch_data()
        return