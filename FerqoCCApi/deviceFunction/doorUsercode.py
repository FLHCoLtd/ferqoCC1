import requests
import json
import time
from ..lib import *
from ..apiDataFormat.device  import *
from ..service.cloud import *
#door configration-------------------------------------------------
def getDoorUserCodeNumber(gatewayInfo, node_id):
    Cmd = deviceExecute(gatewayInfo)
    Cmd.setNodeid(node_id)
    Cmd.getDoorUserCodeNumber()
    data = sendHttp(Cmd.body)
    Cmd = device(gatewayInfo)
    Cmd.setNodeid(node_id)
    data = sendHttp(Cmd.body)
    data = data["payload"]["commands"]
    for j in range(len(data)):
        cmdLen = data[j]["cmdLen"]
        cmd_class = data[j]["cmd_class"]
        cmd = data[j]["cmd"]
        parameter0 = data[j]["parameters"]["0"]
        if (cmd_class == 99 and cmd == 5):
            response = parameter0
    return response
def getDoorUserCode(gatewayInfo, node_id):
    codeNum = getDoorUserCodeNumber(gatewayInfo, node_id)
    usercodetmp = {}
    usercode = []
    usercodetmp["usercode"] = ""
    for i in range(1,codeNum+1):
        Cmd = deviceExecute(gatewayInfo)
        Cmd.setNodeid(node_id)
        Cmd.getDoorUserCode(i)
        data = sendHttp(Cmd.body)
        time.sleep(1)
        Cmd = device(gatewayInfo)
        Cmd.setNodeid(node_id)
        data = sendHttp(Cmd.body)
        data = data["payload"]["commands"]
        for j in range(len(data)):
            cmdLen = data[j]["cmdLen"]
            cmd_class = data[j]["cmd_class"]
            cmd = data[j]["cmd"]
            parameter0 = data[j]["parameters"]["0"]
            parameter1 = data[j]["parameters"]["1"]
            if (cmd_class == 99 and cmd == 3):
                if( parameter0 == i ):
                    usercodetmp["name"] = i
                    if(parameter1 == 0):
                        usercodetmp["status"] = "Available"
                        usercodetmp["usercode"] = "N/A"
                    elif(parameter1 == 1):
                        usercodetmp["status"] = "Occupied"
                        usercodeTrans = ""
                        for k in range(2,cmdLen-2):
                            usercodeTrans = usercodeTrans + chr(data[j]["parameters"][str(k)])
                        usercodetmp["usercode"] = usercodeTrans
                    elif(parameter1 == 2):
                        usercodetmp["status"] = "Reserved by administrator"
                        usercodeTrans = ""
                        for k in range(2,cmdLen-2):
                            usercodeTrans = usercodeTrans + chr(data[j]["parameters"][str(k)])
                        usercodetmp["usercode"] = usercodeTrans
        usercode.append(usercodetmp)
        usercodetmp = {}
    response = usercode
    return response
#-------------------------------------------------