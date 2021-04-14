from service.cloud import *
from service.local import *
from service.FerqoCC import *
from service.httpResPhasing import *
from service.HAType import *
from apiDataFormat.device  import *
from apiDataFormat.scene  import *
from deviceFunction.doorUsercode  import *
from deviceFunction.deviceConfigration import *
gatewayInfo={}
gatewayInfo["gateway_id"] = "011120031"
gatewayInfo["account"] = "admin"
gatewayInfo["password"] = "admin"
#---------cloud api
#---------device Query all
Cmd = device(gatewayInfo)
data = sendHttp(Cmd.body)
DeviceList = dataAnalytics(data)
print(DeviceList)
DeviceList = HAType(DeviceList)
print(DeviceList)
# #---------one device query
# Cmd = device(gatewayInfo)
# Cmd.setNodeid(34)
# data = sendHttp(Cmd.body)
# temp = dataAnalytics(data)
# print(temp)
# #---------device execute
# Cmd = deviceExecute(gatewayInfo)
# Cmd.setNodeid(34)
# Cmd.BlindsAction("stop")
# print(Cmd.body)
# data = sendHttp(Cmd.body)
# print(data)
# #---------scene query
# Cmd = scene(gatewayInfo)
# data = sendHttp(Cmd.body)
# sceneList = sceneAnalytics(data,DeviceList)
# print(sceneList)
# print(Cmd.body)
# #---------scene execute
# Cmd = scene(gatewayInfo)
# Cmd.sceneAction(12)
# print(Cmd.body)
# data = sendHttp(Cmd.body)
# print(data)
# #---------door code
# print(getDoorUserCode(gatewayInfo, 9))
# #---------device configration
# print(getConfigurationCmd(gatewayInfo, 2,10))
# print(setConfigurationCmd(gatewayInfo, 2,10,2,0))
#---------local api
# gatewayInfo = udpBroadcast(gatewayInfo)
# Cmd = device(gatewayInfo)
# gatewayInfo["body"] = Cmd.body
# print(gatewayInfo)