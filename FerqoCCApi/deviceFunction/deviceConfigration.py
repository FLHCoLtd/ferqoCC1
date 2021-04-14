import requests
import json
from FerqoCCApi.apiDataFormat.device  import *
from FerqoCCApi.service.cloud import *
from FerqoCCApi.lib import *

#device configration-------------------------------------------------
def getConfigurationCmd(gatewayInfo, node_id,parameterNum):
    Cmd = deviceExecute(gatewayInfo)
    Cmd.setNodeid(node_id)
    Cmd.getConfigurationCmd(parameterNum)
    sendHttp(Cmd.body)
    Cmd = device(gatewayInfo)
    Cmd.setNodeid(node_id)
    data = sendHttp(Cmd.body)
    response = {}
    data = data["payload"]["commands"]
    response["parameters"] = parameterNum
    for j in range(len(data)):
        cmdLen = data[j]["cmdLen"]
        cmd_class = data[j]["cmd_class"]
        cmd = data[j]["cmd"]
        parameter0 = data[j]["parameters"]["0"]
        parameter1 = data[j]["parameters"]["1"]
        parameter2 = data[j]["parameters"]["2"]
        parameter3 = data[j]["parameters"]["3"]
        parameter4 = data[j]["parameters"]["4"]
        parameter5 = data[j]["parameters"]["5"]
        if (cmd_class == 112 and cmd == 6):
            if( parameter0 == parameterNum ):
                response["Byte"] = parameter1
                if(parameter1 == 1):
                    response["value"] = parameter2
                elif(parameter1 == 2):
                    response["value"] = hexToDec(calculateParameter(parameter2,parameter3))
                elif(parameter1 == 4):
                    tmp = calculateParameter(parameter2,parameter3) + calculateParameter(parameter4,parameter5)
                    response["value"] = hexToDec(tmp)
    return response
def setConfigurationCmd(gatewayInfo, node_id,parameterNum,Byte,value):
    Cmd = deviceExecute(gatewayInfo)
    Cmd.setNodeid(node_id)
    Cmd.setConfigurationCmd(parameterNum,Byte,value)
    data = sendHttp(Cmd.body)
    return data