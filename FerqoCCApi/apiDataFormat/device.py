from ..lib import *
import random, string
class device():
    def __init__(self, gatewayInfo):
        requestId = "FLH-" + ''.join(random.choice(string.ascii_letters + string.digits) for x in range(20))
        self.body = {
                    "requestId": "FLH-11e6b1a064510650abcf",
                    "intent": "action.device.QUERY"
        }
        self.body["requestId"] = requestId
        payload = {}
        self.body["payload"] = payload
        self.body["payload"]["gateway_id"] = gatewayInfo["gateway_id"]
        self.body["payload"]["account"] = gatewayInfo["account"]
        self.body["payload"]["password"] = gatewayInfo["password"]
    def setNodeid(self, nodeid):
        self.body["payload"]["nodeid"] = nodeid

class deviceExecute(device):
    def switchAction(self, cmd):
        self.body["intent"] = "action.device.EXECUTE"
        command = {}
        self.body["payload"]["command"] = command
        self.body["payload"]["command"]["cmdLen"] = 3
        self.body["payload"]["command"]["cmd_class"] = 37
        self.body["payload"]["command"]["cmd"] = 1
        parameters = {}
        self.body["payload"]["command"]["parameters"] = parameters
        if (cmd == "turnOn"):
            self.body["payload"]["command"]["parameters"]["0"] = 255
        elif (cmd == "turnOff"):
            self.body["payload"]["command"]["parameters"]["0"] = 0
    def MultilevelAction(self, cmd):
        self.body["intent"] = "action.device.EXECUTE"
        command = {}
        self.body["payload"]["command"] = command
        self.body["payload"]["command"]["cmdLen"] = 3
        self.body["payload"]["command"]["cmd_class"] = 38
        self.body["payload"]["command"]["cmd"] = 1
        parameters = {}
        self.body["payload"]["command"]["parameters"] = parameters
        if (cmd == "turnOn"):
            self.body["payload"]["command"]["parameters"]["0"] = 255
        elif (cmd == "turnOff"):
            self.body["payload"]["command"]["parameters"]["0"] = 0
        else:
            self.body["payload"]["command"]["parameters"]["0"] = cmd
    def rgbAction(self, cmd):
        self.body["intent"] = "action.device.EXECUTE"
        if (cmd == "turnOn"):
            self.MultilevelAction("turnOn")
        elif (cmd == "turnOff"):
            self.MultilevelAction("turnOff")
        else:
            red = hexToDec( cmd[0] + cmd[1] )
            green = hexToDec( cmd[2] + cmd[3] )
            blue = hexToDec( cmd[4] + cmd[5] )
            command = {}
            self.body["payload"]["command"] = command
            self.body["payload"]["command"]["cmdLen"] = 9
            self.body["payload"]["command"]["cmd_class"] = 51
            self.body["payload"]["command"]["cmd"] = 5
            parameters = {}
            self.body["payload"]["command"]["parameters"] = parameters
            self.body["payload"]["command"]["parameters"]["0"] = 3
            self.body["payload"]["command"]["parameters"]["1"] = 2
            self.body["payload"]["command"]["parameters"]["2"] = red
            self.body["payload"]["command"]["parameters"]["3"] = 3
            self.body["payload"]["command"]["parameters"]["4"] = green
            self.body["payload"]["command"]["parameters"]["5"] = 4
            self.body["payload"]["command"]["parameters"]["6"] = blue
    def BlindsAction(self, cmd):
        self.body["intent"] = "action.device.EXECUTE"
        command = {}
        self.body["payload"]["command"] = command
        self.body["payload"]["command"]["cmdLen"] = 3
        self.body["payload"]["command"]["cmd_class"] = 38
        self.body["payload"]["command"]["cmd"] = 1
        parameters = {}
        self.body["payload"]["command"]["parameters"] = parameters
        if (cmd == "open"):
            self.body["payload"]["command"]["parameters"]["0"] = 255
        elif (cmd == "close"):
            self.body["payload"]["command"]["parameters"]["0"] = 0
        elif (cmd == "stop"):
            self.body["payload"]["command"]["cmdLen"] = 2
            self.body["payload"]["command"]["cmd"] = 5
        else:
            self.body["payload"]["command"]["parameters"]["0"] = cmd
    def irAction(self, cmd, status, temperature="none"):
        self.body["intent"] = "action.device.EXECUTE"
        command = {}
        if(cmd == "mode"):
            self.body["payload"]["command"] = command
            self.body["payload"]["command"]["cmdLen"] = 3
            self.body["payload"]["command"]["cmd_class"] = 64
            self.body["payload"]["command"]["cmd"] = 1
            parameters = {}
            self.body["payload"]["command"]["parameters"] = parameters
            if (status == "cooler"):
                self.body["payload"]["command"]["parameters"]["0"] = 2
            elif (status == "heater"):
                self.body["payload"]["command"]["parameters"]["0"] = 1
            elif (status == "auto"):
                self.body["payload"]["command"]["parameters"]["0"] = 3
            elif (status == "fan"):
                self.body["payload"]["command"]["parameters"]["0"] = 6
            elif (status == "dry"):
                self.body["payload"]["command"]["parameters"]["0"] = 8
            elif (status == "turnOff"):
                self.body["payload"]["command"]["parameters"]["0"] = 0
        elif(cmd == "temperature"):
            self.body["payload"]["command"] = command
            self.body["payload"]["command"]["cmdLen"] = 5
            self.body["payload"]["command"]["cmd_class"] = 67
            self.body["payload"]["command"]["cmd"] = 1
            parameters = {}
            self.body["payload"]["command"]["parameters"] = parameters
            if (status == "cooler"):
                self.body["payload"]["command"]["parameters"]["0"] = 2
            elif (status == "heater"):
                self.body["payload"]["command"]["parameters"]["0"] = 1
            elif (status == "auto"):
                self.body["payload"]["command"]["parameters"]["0"] = 3
            elif (status == "fan"):
                self.body["payload"]["command"]["parameters"]["0"] = 6
            elif (status == "dry"):
                self.body["payload"]["command"]["parameters"]["0"] = 8
            elif (status == "turnOff"):
                self.body["payload"]["command"]["parameters"]["0"] = 0
            self.body["payload"]["command"]["parameters"]["1"] = 1
            if (status != "none"):
                self.body["payload"]["command"]["parameters"]["2"] = temperature
        elif(cmd == "fan"):
            self.body["payload"]["command"] = command
            self.body["payload"]["command"]["cmdLen"] = 3
            self.body["payload"]["command"]["cmd_class"] = 68
            self.body["payload"]["command"]["cmd"] = 1
            parameters = {}
            self.body["payload"]["command"]["parameters"] = parameters
            if (status == "stronger"):
                self.body["payload"]["command"]["parameters"]["0"] = 0
            elif (status == "strong"):
                self.body["payload"]["command"]["parameters"]["0"] = 3
            elif (status == "medium"):
                self.body["payload"]["command"]["parameters"]["0"] = 5
            elif (status == "weak"):
                self.body["payload"]["command"]["parameters"]["0"] = 1
    def doorLockAction(self,cmd):
        self.body["intent"] = "action.device.EXECUTE"
        command = {}
        self.body["payload"]["command"] = command
        self.body["payload"]["command"]["cmdLen"] = 7
        self.body["payload"]["command"]["cmd_class"] = 98
        self.body["payload"]["command"]["cmd"] = 1
        parameters = {}
        self.body["payload"]["command"]["parameters"] = parameters
        if (cmd == "Open"):
            self.body["payload"]["command"]["parameters"]["0"] = 0
        elif (cmd == "Lock"):
            self.body["payload"]["command"]["parameters"]["0"] = 255
        self.body["payload"]["command"]["parameters"]["1"] = 16
        self.body["payload"]["command"]["parameters"]["2"] = 2
        self.body["payload"]["command"]["parameters"]["3"] = 254
        self.body["payload"]["command"]["parameters"]["4"] = 254
    def multiChannelAction(self,channel,cmd):
        self.body["intent"] = "action.device.EXECUTE"
        command = {}
        self.body["payload"]["command"] = command
        self.body["payload"]["command"]["cmdLen"] = 7
        self.body["payload"]["command"]["cmd_class"] = 96
        self.body["payload"]["command"]["cmd"] = 13
        parameters = {}
        self.body["payload"]["command"]["parameters"] = parameters
        if (cmd == "turnOn"):
            self.body["payload"]["command"]["parameters"]["4"] = 255
        elif (cmd == "turnOff"):
            self.body["payload"]["command"]["parameters"]["4"] = 0
        self.body["payload"]["command"]["parameters"]["0"] = 0
        self.body["payload"]["command"]["parameters"]["1"] = channel
        self.body["payload"]["command"]["parameters"]["2"] = 37
        self.body["payload"]["command"]["parameters"]["3"] = 1
    def getConfigurationCmd(self, parameterNum):
        self.body["intent"] = "action.device.EXECUTE"
        command = {}
        self.body["payload"]["command"] = command
        self.body["payload"]["command"]["cmdLen"] = 3
        self.body["payload"]["command"]["cmd_class"] = 112
        self.body["payload"]["command"]["cmd"] = 5
        parameters = {}
        self.body["payload"]["command"]["parameters"] = parameters
        self.body["payload"]["command"]["parameters"]["0"] = parameterNum
    def setConfigurationCmd(self, parameterNum,Byte,value):
        self.body["intent"] = "action.device.EXECUTE"
        command = {}
        self.body["payload"]["command"] = command
        self.body["payload"]["command"]["cmdLen"] = Byte + 4
        self.body["payload"]["command"]["cmd_class"] = 112
        self.body["payload"]["command"]["cmd"] = 4
        parameters = {}
        self.body["payload"]["command"]["parameters"] = parameters
        self.body["payload"]["command"]["parameters"]["0"] = parameterNum
        self.body["payload"]["command"]["parameters"]["1"] = Byte
        tmp = str(decToHex(value))
        for i in range(8-len(tmp)):
            tmp = "0" + tmp
        if(Byte == 1):
            self.body["payload"]["command"]["parameters"]["2"] = hexToDec(tmp[6] + tmp[7])
        elif(Byte == 2):
            self.body["payload"]["command"]["parameters"]["2"] = hexToDec(tmp[4] + tmp[5])
            self.body["payload"]["command"]["parameters"]["3"] = hexToDec(tmp[6] + tmp[7]) 
        elif(Byte == 4):
            self.body["payload"]["command"]["parameters"]["2"] = hexToDec(tmp[0] + tmp[1])
            self.body["payload"]["command"]["parameters"]["3"] = hexToDec(tmp[2] + tmp[3])
            self.body["payload"]["command"]["parameters"]["4"] = hexToDec(tmp[4] + tmp[5])
            self.body["payload"]["command"]["parameters"]["5"] = hexToDec(tmp[6] + tmp[7])
    def getDoorUserCodeNumber(self):
        self.body["intent"] = "action.device.EXECUTE"
        command = {}
        self.body["payload"]["command"] = command
        self.body["payload"]["command"]["cmdLen"] = 2
        self.body["payload"]["command"]["cmd_class"] = 99
        self.body["payload"]["command"]["cmd"] = 4
    def getDoorUserCode(self,i):
        self.body["intent"] = "action.device.EXECUTE"
        command = {}
        self.body["payload"]["command"] = command
        self.body["payload"]["command"]["cmdLen"] = 3
        self.body["payload"]["command"]["cmd_class"] = 99
        self.body["payload"]["command"]["cmd"] = 2
        parameters = {}
        self.body["payload"]["command"]["parameters"] = parameters
        self.body["payload"]["command"]["parameters"]["0"] = i