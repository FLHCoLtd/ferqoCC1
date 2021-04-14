from ..lib import *



def dataAnalytics(data):
    deviceList = []
    deviceTemp = {}
    if (str(data["payload"].get("devicesCount")) == "None"):
        deviceTemp["name"] = data["payload"]["node_name"]
        deviceTemp["node_id"] = data["payload"]["node_id"]
        basic = data["payload"]["basic"]
        generic = data["payload"]["generic"]
        specific = data["payload"]["specific"]
        if (basic == 4):
            if (generic == 16 and specific == 1):
                deviceTemp["type"] = "Binary Power Switch"
                deviceTemp["HAtype"] = "light"
                deviceTemp["subType"] = "switch"
            elif (generic == 17):
                if (specific == 1):
                    deviceTemp["type"] = "Multilevel Power Switch"
                    deviceTemp["HAtype"] = "light"
                    deviceTemp["subType"] = "multilevel"
                if (specific == 2):
                    deviceTemp["type"] = "Color Tunable Multilevel"
                    deviceTemp["HAtype"] = "light"
                    deviceTemp["subType"] = "multilevel"
                elif (specific == 6):
                    deviceTemp["type"] = "Motor Control B"
                    deviceTemp["HAtype"] = "cover"
            elif (generic == 24 and specific == 1):
                deviceTemp["type"] = "Basic Wall Controller"
                deviceTemp["HAtype"] = "switch"
            elif (generic == 7 and specific == 1):
                deviceTemp["type"] = "Notification Sensor"
                deviceTemp["HAtype"] = "sensor"
            elif (generic == 33 and specific == 1):
                deviceTemp["type"] = "Multilevel Sensor"
                deviceTemp["HAtype"] = "sensor"
            elif (generic == 64 and specific == 3):
                deviceTemp["type"] = "Secure Keypad Door Lock"
                deviceTemp["HAtype"] = "lock"
            elif (generic == 8 and specific == 6):
                deviceTemp["type"] = "IR"
                deviceTemp["HAtype"] = "ir"
            else:
                deviceTemp["type"] = "unknown"
        else:
            deviceTemp["type"] = "unknown"
        cmdData = data["payload"]["commands"]
        deviceTemp = cmdClassAnalytics(cmdData,deviceTemp)
        deviceList.append(deviceTemp)
        deviceTemp = {}
    else:
        for i in range(data["payload"]["devicesCount"]):
            deviceTemp["name"] = data["payload"]["devices"][i]["node_name"]
            deviceTemp["node_id"] = data["payload"]["devices"][i]["node_id"]
            basic = data["payload"]["devices"][i]["basic"]
            generic = data["payload"]["devices"][i]["generic"]
            specific = data["payload"]["devices"][i]["specific"]
            if (basic == 4):
                if (generic == 16 and specific == 1):
                    deviceTemp["type"] = "Binary Power Switch"
                    deviceTemp["HAtype"] = "light"
                    deviceTemp["subType"] = "switch"
                elif (generic == 17):
                    if (specific == 1):
                        deviceTemp["type"] = "Multilevel Power Switch"
                        deviceTemp["HAtype"] = "light"
                        deviceTemp["subType"] = "multilevel"
                    if (specific == 2):
                        deviceTemp["type"] = "Color Tunable Multilevel"
                        deviceTemp["HAtype"] = "light"
                        deviceTemp["subType"] = "multilevel"
                    elif (specific == 6):
                        deviceTemp["type"] = "Motor Control B"
                        deviceTemp["HAtype"] = "cover"
                elif (generic == 24 and specific == 1):
                    deviceTemp["type"] = "Basic Wall Controller"
                    deviceTemp["HAtype"] = "switch"
                elif (generic == 7 and specific == 1):
                    deviceTemp["type"] = "Notification Sensor"
                    deviceTemp["HAtype"] = "sensor"
                elif (generic == 33 and specific == 1):
                    deviceTemp["type"] = "Multilevel Sensor"
                    deviceTemp["HAtype"] = "sensor"
                elif (generic == 64 and specific == 3):
                    deviceTemp["type"] = "Secure Keypad Door Lock"
                    deviceTemp["HAtype"] = "lock"
                elif (generic == 8 and specific == 6):
                    deviceTemp["type"] = "IR"
                    deviceTemp["HAtype"] = "ir"
                else:
                    deviceTemp["type"] = "unknown"
            else:
                deviceTemp["type"] = "unknown"
            cmdData = data["payload"]["devices"][i]["commands"]
            deviceTemp = cmdClassAnalytics(cmdData,deviceTemp)
            deviceList.append(deviceTemp)
            deviceTemp = {}
    return deviceList
def cmdClassAnalytics(data,deviceTemp):
    red = "00"
    green = "00"
    blue = "00"
    multiChannel = []
    multiChannelTmp = {}
    sensorValue = []
    valuetemp = {}
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
        parameter6 = data[j]["parameters"]["6"]
        parameter7 = data[j]["parameters"]["7"]
        parameter8 = data[j]["parameters"]["8"]
        if (cmdLen == 8 and cmd_class == 114 and cmd == 5):
            ManufacturerId = calculateParameter(parameter0,parameter1)
            productTypeId = calculateParameter(parameter2,parameter3)
            if (ManufacturerId == "010f") :
                deviceTemp["Manufacturer"] = "Fibargroup"
                if (productTypeId == "0403") :
                    deviceTemp["product"] = "single switch 2"
                    deviceTemp["HAtype"] = "light"
                elif (productTypeId == "0102") :
                    deviceTemp["product"] = "dimmer 2"
                    deviceTemp["HAtype"] = "light"
                elif (productTypeId == "0902") :
                    deviceTemp["product"] = "RGBW Controller 2"
                    deviceTemp["HAtype"] = "light"
                elif (productTypeId == "0f01") :
                    deviceTemp["product"] = "the button"
                    deviceTemp["HAtype"] = "scene controller"
                elif (productTypeId == "0900") :
                    deviceTemp["product"] = "RGBW Controller"
                    deviceTemp["HAtype"] = "light"
                elif (productTypeId == "0801") :
                    deviceTemp["product"] = "motion sensor"
                    deviceTemp["HAtype"] = "sensor"
                elif (productTypeId == "0c02") :
                    deviceTemp["product"] = "smoke sensor"
                    deviceTemp["HAtype"] = "sensor"
                elif (productTypeId == "0b01") :
                    deviceTemp["product"] = "flood sensor"
                    deviceTemp["HAtype"] = "sensor"
                elif (productTypeId == "0502") :
                    deviceTemp["product"] = "smart implant"
                    deviceTemp["HAtype"] = "sensor"
                elif (productTypeId == "1701") :
                    deviceTemp["product"] = "wallplug"
                    deviceTemp["HAtype"] = "switch"
                elif (productTypeId == "0702") :
                    deviceTemp["product"] = "Door/window sensor"
                    deviceTemp["HAtype"] = "sensor"
                elif (productTypeId == "1001") :
                    deviceTemp["product"] = "Keyfod"
                    deviceTemp["HAtype"] = "scene controller"
                elif (productTypeId == "0d01") :
                    deviceTemp["product"] = "Swipe"
                    deviceTemp["HAtype"] = "scene controller"
                elif (productTypeId == "0303") :
                    deviceTemp["product"] = "Roller shutter 3"
                    deviceTemp["HAtype"] = "cover"
            elif (ManufacturerId == "015f") :   
                deviceTemp["Manufacturer"] = "McoHome Technology Co., Ltd"
                if (productTypeId == "0901") :
                    deviceTemp["product"] = "MCO CO2"
                    deviceTemp["HAtype"] = "sensor"
                elif (productTypeId == "0a01") :
                    deviceTemp["product"] = "MCO pm2.5"
                    deviceTemp["HAtype"] = "sensor"
                elif (productTypeId == "3112") :
                    deviceTemp["product"] = "Touch Panel Switch no-n 1ch"
                    deviceTemp["HAtype"] = "light"
                    deviceTemp["subType"] = "switch"
                elif (productTypeId == "3122") :
                    deviceTemp["product"] = "Touch Panel Switch no-n 2ch"
                    deviceTemp["HAtype"] = "light"
                    deviceTemp["subType"] = "switch"
                elif (productTypeId == "5112") :
                    deviceTemp["product"] = "Touch Panel Switch 1ch"
                    deviceTemp["HAtype"] = "light"
                    deviceTemp["subType"] = "switch"
                elif (productTypeId == "5121") :
                    deviceTemp["product"] = "Touch Panel Switch 2ch"
                    deviceTemp["HAtype"] = "light"
                    deviceTemp["subType"] = "switch"
                elif (productTypeId == "5131") :
                    deviceTemp["product"] = "Touch Panel Switch 3ch"
                    deviceTemp["HAtype"] = "light"
                    deviceTemp["subType"] = "switch"
            elif (ManufacturerId == "013c") :   
                deviceTemp["Manufacturer"] = "Philio Technology Corp"
                if (productTypeId == "0001") :
                    deviceTemp["product"] = "Philio wallplug"
                    deviceTemp["HAtype"] = "switch"
                elif (productTypeId == "0102") :
                    deviceTemp["product"] = "Philio ir par01"
                    deviceTemp["HAtype"] = "ir"
            elif (ManufacturerId == "0129") :   
                deviceTemp["Manufacturer"] = "ASSA ABLOY"
                if (productTypeId == "c700") :
                    deviceTemp["product"] = "Yale door Lock"
                    deviceTemp["HAtype"] = "lock"
        if (cmdLen == 3 and cmd_class == 37 and cmd == 3):
            if (parameter0 == 0):
                deviceTemp["status"] = "OFF"
            elif (parameter0 > 0):
                deviceTemp["status"] = "ON"
        if (cmd_class == 50 and cmd == 2):
            if (parameter0 == 33):
                tmp = decToBin(parameter1)
                precision = binToDec(tmp[0] + tmp[1] + tmp[2])
                scale = binToDec(tmp[3] + tmp[4])
                byte = binToDec(tmp[5] + tmp[6] + tmp[7])
                precision = 10 ** precision
                if(scale == 0):
                    powerUnit = "kWh"
                elif(scale == 1):
                    powerUnit = "kVAh"
                elif(scale == 2):
                    powerUnit = "W"
                elif(scale == 4):
                    powerUnit = "V"
                elif(scale == 5):
                    powerUnit = "A"
                if(byte == 1):
                    power = hexToDec(parameter2)
                    deviceTemp["power"] = str(power / precision ) + powerUnit;
                elif(byte == 2):
                    powerNow = hexToDec(calculateParameter(parameter2,parameter3))
                    deviceTemp["powerNow"] = str(powerNow / precision ) + powerUnit
                elif(byte == 4):
                    powerTotal = hexToDec(calculateParameter(parameter2,parameter3) + calculateParameter(parameter4,parameter5))
                    deviceTemp["powerTotal"] = str(powerTotal / precision ) + powerUnit
                else:
                    deviceTemp["list"] = "out"
        if (cmdLen == 5 and cmd_class == 91 and cmd == 3):
            tmp = decToBin(parameter1)
            key = binToDec(tmp[5] + tmp[6] + tmp[7])
            if ( key == 0):
                deviceTemp["actionStatus"] = "pressed 1"
            elif ( key == 1):
                deviceTemp["actionStatus"] = "released"
            elif ( key == 2):
                deviceTemp["actionStatus"] = "Held down"
            elif ( key == 3):
                deviceTemp["actionStatus"] = "pressed 2"
            elif ( key == 4):
                deviceTemp["actionStatus"] = "pressed 3"
            elif ( key == 5):
                deviceTemp["actionStatus"] = "pressed 4"
            elif ( key == 6):
                deviceTemp["actionStatus"] = "pressed 5"
            if ( parameter2 == 1):
                deviceTemp["button"] = "scene1"
            elif ( parameter2 == 2):
                deviceTemp["button"] = "scene2"
            elif ( parameter2 == 3):
                deviceTemp["button"] = "scene3"
            elif ( parameter2 == 4):
                deviceTemp["button"] = "scene4"
            elif ( parameter2 == 5):
                deviceTemp["button"] = "scene5"
            elif ( parameter2 == 6):
                deviceTemp["button"] = "scene6"
        if (cmdLen == 3 and cmd_class == 38 and cmd == 3):
            if (deviceTemp["type"] == "Multilevel Power Switch"):
                if (parameter0 == 0):
                    deviceTemp["status"] = "OFF"
                    deviceTemp["brightness"] = "0"
                elif (parameter0 > 0):
                    if (parameter0 >= 99):
                        parameter0 = 100
                    deviceTemp["status"] = "ON"
                    deviceTemp["brightness"] = str(parameter0)
            if (deviceTemp["type"] == "Color Tunable Multilevel"):
                if (parameter0 == 0):
                    deviceTemp["status"] = "OFF"
                    deviceTemp["brightness"] = "0"
                elif (parameter0 > 0):
                    if (parameter0 >= 99):
                        parameter0 = 100
                    deviceTemp["status"] = "ON"
                    deviceTemp["brightness"] = str(parameter0)
            if (deviceTemp["type"] == "Motor Control B"):
                if (parameter0 == 0):
                    deviceTemp["status"] = "Open"
                elif (parameter0 > 0):
                    if (parameter0 >= 99):
                        deviceTemp["status"] = "Close"
                    else:
                        deviceTemp["status"] = str(parameter0) + "%"
        if (cmd_class == 51 and cmd == 4):
            if (parameter0 == 2):
                red = decToHex(parameter1)
            elif (parameter0 == 3):
                green = decToHex(parameter1)
            elif (parameter0 == 4):
                blue = decToHex(parameter1)
            deviceTemp["color"] = str(red) + str(green) + str(blue)
        if (cmdLen == 3 and cmd_class == 128 and cmd == 3):
            deviceTemp["battery"] = str(parameter0) + "%"
        if (cmd_class == 96 and cmd == 13):
            channelName = str(parameter0) 
            multiChannelTmp["channelName"] = channelName
            if (parameter2 == 113 and parameter3 == 5):
                multiChannelTmp["signal"] = "input"
                if (parameter7 == 0):
                    multiChannelTmp["status"] = "safe"
                elif (parameter7 > 0):
                    multiChannelTmp["status"] = "breach"
            elif (parameter2 == 37 and parameter3 == 3):
                multiChannelTmp["signal"] = "output"
                if (parameter4 == 0):
                    multiChannelTmp["status"] = "OFF"
                elif (parameter4 > 0):
                    multiChannelTmp["status"] = "ON"
            multiChannel.append(multiChannelTmp)
            deviceTemp["multiChannel"] = multiChannel
            multiChannelTmp = {}
        if (cmdLen == 7 and cmd_class == 98 and cmd == 3):
            if (parameter0 == 0):
                deviceTemp["status"] = "Open"
            elif (parameter0 == 255):
                deviceTemp["status"] = "Lock"
        if (cmd_class == 49 and cmd == 5):
            parameter0 = decToHex(parameter0)
            tmp = decToBin(parameter1)
            precision = binToDec(tmp[0] + tmp[1] + tmp[2])
            scale = binToDec(tmp[3] + tmp[4])
            byte = binToDec(tmp[5] + tmp[6] + tmp[7])
            precision = 10 ** precision
            if ( parameter0 == "01"): #temperature
                sensorName = "temperature"
                if(scale == 0):
                    sensorUnit = "°C"
                elif(scale == 1):
                    sensorUnit = "°F"
            elif ( parameter0 == "04"):#power
                sensorName = "power"
                if(scale == 0):
                    sensorUnit = "W"
                elif(scale == 1):
                    sensorUnit = "Btu/h"
            elif ( parameter0 == "05"):#humidity
                sensorName = "humidity"
                if(scale == 0):
                    sensorUnit = "%"
                elif(scale == 1):
                    sensorUnit = "g/m3"
            elif ( parameter0 == "03"): #lux
                sensorName = "lux"
                if(scale == 0):
                    sensorUnit = "%"
                elif(scale == 1):
                    sensorUnit = "lux"
            elif ( parameter0 == "11"):#co2
                sensorName = "co2"
                if(scale == 0):
                    sensorUnit = "ppm"
            elif ( parameter0 == "19"):#Seismic Intensity
                sensorName = "Seismic Intensity"
                if(scale == 0):
                    sensorUnit = "Mercalli"
                elif(scale == 1):
                    sensorUnit = "European Macroseismic"
            elif ( parameter0 == "23"):#pm2.5
                sensorName = "pm2.5"
                if(scale == 0):
                    sensorUnit = "mol/m3"
                elif(scale == 1):
                    sensorUnit = "µg/m3"
            elif ( parameter0 == "34"):#Acceleration X-axis
                sensorName = "Acceleration X-axis"
                if(scale == 0):
                    sensorUnit = "m/s2"
            elif ( parameter0 == "35"):#Acceleration Y-axis
                sensorName = "Acceleration Y-axis"
                if(scale == 0):
                    sensorUnit = "m/s2"
            elif ( parameter0 == "36"):#Acceleration Z-axis
                sensorName = "Acceleration Z-axis"
                if(scale == 0):
                    sensorUnit = "m/s2"
            if(byte == 1):
                value = parameter2
                valuetemp[str(sensorName)] = str(value / precision)
                valuetemp["sensorType"] = sensorName
                valuetemp["sensorUnit"] = str(sensorUnit)
                sensorValue.append(valuetemp)
                deviceTemp["sensorValue"] = sensorValue
                valuetemp = {}
            elif(byte == 2):
                value = hexToDec(calculateParameter(parameter2,parameter3))
                valuetemp["sensorType"] = sensorName
                valuetemp[str(sensorName)] = str(value / precision)
                valuetemp["sensorUnit"] = str(sensorUnit)
                sensorValue.append(valuetemp)
                deviceTemp["sensorValue"] = sensorValue
                valuetemp = {}
            elif(byte == 4):
                value = hexToDec(calculateParameter(parameter2,parameter3) + calculateParameter(parameter4,parameter5))
                valuetemp["sensorType"] = sensorName
                valuetemp[str(sensorName)] = str(value / precision)
                valuetemp["sensorUnit"] = str(sensorUnit)
                sensorValue.append(valuetemp)
                deviceTemp["sensorValue"] = sensorValue
                valuetemp = {}
        if (cmdLen == 3 and cmd_class == 32 and cmd == 1):
            if (parameter0 == 0):
                deviceTemp["sensorStatus"] = "safe"
            elif (parameter0 > 0):
                deviceTemp["sensorStatus"] = "breach"
        if (cmdLen == 11 and cmd_class == 255 and cmd == 255):
            deviceTemp["extension_gateway"] = chr(parameter0) + chr(parameter1) + chr(parameter2) + chr(parameter3) + chr(parameter4) + chr(parameter5) + chr(parameter6) + chr(parameter7) + chr(parameter8)
        if (cmdLen == 3 and cmd_class == 64 and cmd == 3):
            if (parameter0 == 0):
                deviceTemp["IRmode"] = "turnOff"
            elif (parameter0 == 1):
                deviceTemp["IRmode"] = "heater"
            elif (parameter0 == 2):
                deviceTemp["IRmode"] = "cooler"
            elif (parameter0 == 3):
                deviceTemp["IRmode"] = "auto"
            elif (parameter0 == 6):
                deviceTemp["IRmode"] = "fan"
            elif (parameter0 == 8):
                deviceTemp["IRmode"] = "dry"
    return deviceTemp
def cmdclas143(data,cmdLen):
    cmdList = []
    cmdTemp = {}
    parameterTemp = {}
    i = 1
    while i < cmdLen-2:
        cmdTemp["cmdLen"] = data[str(i)]
        cmdTemp["cmd_class"] = data[str(i + 1)]
        cmdTemp["cmd"] = data[str(i + 2)]
        i = i + 3
        for j in range(0,cmdTemp["cmdLen"]-2):
            k=i+j
            parameterTemp[str(j)] = data[str(k)]
        i = i + cmdTemp["cmdLen"] - 2
        cmdTemp["parameters"] = parameterTemp
        cmdList.append(cmdTemp)
        cmdTemp = {}
        parameterTemp = {}
    return cmdList
def sceneActionCmdClass(data,actionTemp):
    red = "00"
    green = "00"
    blue = "00"
    cmdLen = data["cmdLen"]
    cmd_class = data["cmd_class"]
    cmd = data["cmd"]
    parameter0 = data["parameters"]["0"]
    parameter1 = data["parameters"]["1"]
    parameter2 = data["parameters"]["2"]
    parameter3 = data["parameters"]["3"]
    parameter4 = data["parameters"]["4"]
    parameter5 = data["parameters"]["5"]
    if (cmdLen == 3 and cmd_class == 37 and cmd == 1):
        if (parameter0 == 255):
            actionTemp["action"] = "turnOn"
        elif (parameter0 == 0):
            actionTemp["action"] = "turnOff"
    elif (cmdLen == 3 and cmd_class == 38 and cmd == 1):
        if (actionTemp["type"] == "Motor Control B"):
            if (parameter0 == 255):
                actionTemp["action"] = "open"
            elif (parameter0 == 0):
                actionTemp["action"] = "close"
            elif (parameter0 > 0 and parameter0 < 100):
                actionTemp["action"] = "open ," + str(parameter0) + "%"
        elif (actionTemp["type"] == "Multilevel Power Switch"):
            if (parameter0 == 255):
                actionTemp["action"] = "turnOn"
            elif (parameter0 == 0):
                actionTemp["action"] = "turnOff"
            elif (parameter0 > 0 and parameter0 < 100):
                actionTemp["action"] = "turnOn ," + str(parameter0) + "%"
    elif (cmd_class == 143 and cmd == 1):
        data = data["parameters"]
        tmpParameter = cmdclas143(data,cmdLen)
        for i in range(len(tmpParameter)):
            cmdLen = tmpParameter[i]["cmdLen"]
            cmd_class = tmpParameter[i]["cmd_class"]
            cmd = tmpParameter[i]["cmd"]
            parameter0 = tmpParameter[i]["parameters"]["0"]
            if(cmd_class == 51 and cmd == 5):
                for j in range(1,cmdLen-2,2):
                    parametertmp1 = tmpParameter[i]["parameters"][str(j)]
                    parametertmp2 = tmpParameter[i]["parameters"][str(j+1)]
                    if (parametertmp1 == 2):
                        red = decToHex(parametertmp2)
                    elif (parametertmp1 == 3):
                        green = decToHex(parametertmp2)
                    elif (parametertmp1 == 4):
                        blue = decToHex(parametertmp2)
                    actionTemp["color"] = str(red) + str(green) + str(blue)
            if(cmdLen == 3 and cmd_class == 38 and cmd == 1):
                if (parameter0 == 255):
                    actionTemp["action"] = "turnOn"
                elif (parameter0 == 0):
                    actionTemp["action"] = "turnOff"
                elif (parameter0 > 0 and parameter0 < 100):
                    actionTemp["action"] = "turnOn ," + str(parameter0) + "%"
    elif (cmdLen == 3 and cmd_class == 64 and cmd == 1):
        if (parameter0 == 0):
            actionTemp["mode"] = "turnOff"
        elif (parameter0 == 1):
            actionTemp["mode"] = "heater"
        elif (parameter0 == 2):
            actionTemp["mode"] = "cooler"
        elif (parameter0 == 3):
            actionTemp["mode"] = "auto"
        elif (parameter0 == 6):
            actionTemp["mode"] = "fan"
        elif (parameter0 == 8):
            actionTemp["mode"] = "dry"
    elif (cmdLen == 5 and cmd_class == 67 and cmd == 1):
        if (parameter0 == 0):
            actionTemp["mode"] = "turnOff"
        elif (parameter0 == 1):
            actionTemp["mode"] = "heater"
        elif (parameter0 == 2):
            actionTemp["mode"] = "cooler"
        elif (parameter0 == 3):
            actionTemp["mode"] = "auto"
        elif (parameter0 == 6):
            actionTemp["mode"] = "fan"
        elif (parameter0 == 8):
            actionTemp["mode"] = "dry"
        actionTemp["temperature"] = parameter2
    elif (cmdLen == 3 and cmd_class == 68 and cmd == 1):
        if (parameter0 == 0):
            actionTemp["fan"] = "stronger"
        elif (parameter0 == 3):
            actionTemp["fan"] = "strong"
        elif (parameter0 == 5):
            actionTemp["fan"] = "medium"
        elif (parameter0 == 1):
            actionTemp["fan"] = "weak"
    return actionTemp
def sceneEnventCmdClass(data,eventTemp):
    red = "00"
    green = "00"
    blue = "00"
    multiChannel = []
    multiChannelTmp = {}
    cmdLen = data["cmdLen"]
    cmd_class = data["cmd_class"]
    cmd = data["cmd"]
    parameter0 = data["parameters"]["0"]
    parameter1 = data["parameters"]["1"]
    parameter2 = data["parameters"]["2"]
    parameter3 = data["parameters"]["3"]
    parameter4 = data["parameters"]["4"]
    parameter5 = data["parameters"]["5"]
    parameter6 = data["parameters"]["6"]
    parameter7 = data["parameters"]["7"]
    if (cmdLen == 3 and cmd_class == 37 and cmd == 3):
        if (parameter0 == 0):
            eventTemp["status"] = "OFF"
        elif (parameter0 > 0):
            eventTemp["status"] = "ON"
    if (cmd_class == 50 and cmd == 2):
        if (parameter0 == 33):
            tmp = decToBin(parameter1)
            precision = binToDec(tmp[0] + tmp[1] + tmp[2])
            scale = binToDec(tmp[3] + tmp[4])
            byte = binToDec(tmp[5] + tmp[6] + tmp[7])
            precision = 10 ** precision
            if(scale == 0):
                unit = "kWh"
            elif(scale == 1):
                unit = "kVAh"
            elif(scale == 2):
                unit = "W"
            elif(scale == 4):
                unit = "V"
            elif(scale == 5):
                unit = "A"
            if(byte == 1):
                power = hexToDec(parameter2)
                eventTemp["power"] = str(power / precision ) + unit;
            elif(byte == 2):
                powerNow = hexToDec(calculateParameter(parameter2,parameter3))
                eventTemp["powerNow"] = str(powerNow / precision ) + unit;
            elif(byte == 4):
                powerTotal = hexToDec(calculateParameter(parameter2,parameter3) + calculateParameter(parameter4,parameter5))
                eventTemp["powerTotal"] = str(powerTotal / precision ) + unit;
    if (cmdLen == 5 and cmd_class == 91 and cmd == 3):
        tmp = decToBin(parameter1)
        key = binToDec(tmp[5] + tmp[6] + tmp[7])
        if ( key == 0):
            eventTemp["status"] = "pressed 1"
        elif ( key == 1):
            eventTemp["status"] = "released"
        elif ( key == 2):
            eventTemp["status"] = "Held down"
        elif ( key == 3):
            eventTemp["status"] = "pressed 2"
        elif ( key == 4):
            eventTemp["status"] = "pressed 3"
        elif ( key == 5):
            eventTemp["status"] = "pressed 4"
        elif ( key == 6):
            eventTemp["status"] = "pressed 5"
        if ( parameter2 == 1):
            eventTemp["button"] = "scene1"
        elif ( parameter2 == 2):
            eventTemp["button"] = "scene2"
        elif ( parameter2 == 3):
            eventTemp["button"] = "scene3"
        elif ( parameter2 == 4):
            eventTemp["button"] = "scene4"
        elif ( parameter2 == 5):
            eventTemp["button"] = "scene5"
        elif ( parameter2 == 6):
            eventTemp["button"] = "scene6"
    if (cmdLen == 3 and cmd_class == 38 and cmd == 3):
        if (eventTemp["type"] == "Multilevel Power Switch"):
            if (parameter0 == 0):
                eventTemp["status"] = "OFF"
            elif (parameter0 > 0):
                if (parameter0 == 99):
                    parameter0 = 100
                eventTemp["status"] = str(parameter0) + "%"
        if (eventTemp["type"] == "Motor Control B"):
            if (parameter0 == 0):
                eventTemp["status"] = "Close"
            elif (parameter0 > 0):
                if (parameter0 >= 99):
                    eventTemp["status"] = "Open"
                else:
                    eventTemp["status"] = str(parameter0) + "%"
    if (cmdLen == 4 and cmd_class == 51 and cmd == 4):
        if (parameter0 == 2):
            red = decToHex(parameter1)
        elif (parameter0 == 3):
            green = decToHex(parameter1)
        elif (parameter0 == 4):
            blue = decToHex(parameter1)
        eventTemp["color"] = str(red) + str(green) + str(blue)
    if (cmdLen == 3 and cmd_class == 128 and cmd == 3):
        eventTemp["battery"] = str(parameter0) + "%"
    if (cmd_class == 49 and cmd == 5):
            parameter0 = decToHex(parameter0)
            tmp = decToBin(parameter1)
            precision = binToDec(tmp[0] + tmp[1] + tmp[2])
            scale = binToDec(tmp[3] + tmp[4])
            byte = binToDec(tmp[5] + tmp[6] + tmp[7])
            precision = 10 ** precision
            if ( parameter0 == "01"): #temperature
                sensorName = "temperature"
                if(scale == 0):
                    sensorUnit = "C"
                elif(scale == 1):
                    sensorUnit = "F"
            elif ( parameter0 == "04"):#power
                sensorName = "power"
                if(scale == 0):
                    sensorUnit = "W"
                elif(scale == 1):
                    sensorUnit = "Btu/h"
            elif ( parameter0 == "05"):#humidity
                sensorName = "humidity"
                if(scale == 0):
                    sensorUnit = "%"
                elif(scale == 1):
                    sensorUnit = "g/m3"
            elif ( parameter0 == "03"): #lux
                sensorName = "lux"
                if(scale == 0):
                    sensorUnit = "%"
                elif(scale == 1):
                    sensorUnit = "lux"
            elif ( parameter0 == "11"):#co2
                sensorName = "co2"
                if(scale == 0):
                    sensorUnit = "ppm"
            elif ( parameter0 == "19"):#Seismic Intensity
                sensorName = "Seismic Intensity"
                if(scale == 0):
                    sensorUnit = "Mercalli"
                elif(scale == 1):
                    sensorUnit = "European Macroseismic"
            elif ( parameter0 == "23"):#pm2.5
                sensorName = "pm2.5"
                if(scale == 0):
                    sensorUnit = "mol/m3"
                elif(scale == 1):
                    sensorUnit = "µg/m3"
            elif ( parameter0 == "34"):#Acceleration X-axis
                sensorName = "Acceleration X-axis"
                if(scale == 0):
                    sensorUnit = "m/s2"
            elif ( parameter0 == "35"):#Acceleration Y-axis
                sensorName = "Acceleration Y-axis"
                if(scale == 0):
                    sensorUnit = "m/s2"
            elif ( parameter0 == "36"):#Acceleration Z-axis
                sensorName = "Acceleration Z-axis"
                if(scale == 0):
                    sensorUnit = "m/s2"
            if(byte == 1):
                value = parameter2
                eventTemp[str(sensorName)] = str(value / precision) + str(sensorUnit)
            elif(byte == 2):
                value = hexToDec(calculateParameter(parameter2,parameter3))
                eventTemp[str(sensorName)] = str(value / precision) + str(sensorUnit)
            elif(byte == 4):
                value = hexToDec(calculateParameter(parameter2,parameter3) + calculateParameter(parameter4,parameter5))
                eventTemp[str(sensorName)] = str(value / precision) + str(sensorUnit)
            else:
                eventTemp["list"] = "list out"
    if (cmdLen == 3 and cmd_class == 32 and cmd == 1):
        if (parameter0 == 0):
            eventTemp["sensorStatus"] = "safe"
        elif (parameter0 > 0):
            eventTemp["sensorStatus"] = "breach"
    if (cmd_class == 96 and cmd == 13):
        channelName = str(parameter0) 
        multiChannelTmp["channelName"] = channelName
        if (parameter2 == 113 and parameter3 == 5):
            multiChannelTmp["signal"] = "input"
            if (parameter7 == 0):
                multiChannelTmp["status"] = "safe"
            elif (parameter7 > 0):
                multiChannelTmp["status"] = "breach"
        elif (parameter2 == 37 and parameter3 == 3):
            multiChannelTmp["signal"] = "output"
            if (parameter4 == 0):
                multiChannelTmp["status"] = "OFF"
            elif (parameter4 > 0):
                multiChannelTmp["status"] = "ON"
        multiChannel.append(multiChannelTmp)
        eventTemp["multiChannel"] = multiChannel
        multiChannelTmp = {}
    if (cmdLen == 7 and cmd_class == 98 and cmd == 3):
            if (parameter0 == 0):
                eventTemp["status"] = "Open"
            elif (parameter0 == 255):
                eventTemp["status"] = "Lock"
    return eventTemp
def sceneAnalytics(data):
    sceneList = []
    sceneTemp = {}
    actionTemp = {}
    action = []
    eventTemp = {}
    event = []
    eventDeviceTP = {}
    for i in range(len(data["payload"]["sceneList"])): 
        sceneTemp["name"] = data["payload"]["sceneList"][i]["sceneName"]
        sceneTemp["sceneId"] = data["payload"]["sceneList"][i]["sceneId"]
        # data["payload"]["sceneList"][i]["events"]
        # eventData = data["payload"]["sceneList"][i]["events"]
        # actionData = data["payload"]["sceneList"][i]["actions"]
        # for j in range(len(eventData)):
        #     eventTemp["node_id"] = eventData[j]["node_id"]
        #     serchDevice(deviceInfoData,eventTemp)
        #     Data = eventData[j]
        #     eventTemp = sceneEnventCmdClass(Data,eventTemp)
        #     event.append(eventTemp)
        #     eventTemp = {}
        # sceneTemp["event"] = event
        # event=[]
        # for j in range(len(actionData)):
        #     actionTemp["node_id"] = actionData[j]["node_id"]
        #     actionTemp["duration"] = actionData[j]["duration"]
        #     serchDevice(deviceInfoData,actionTemp)
        #     Data = actionData[j]
        #     actionTemp = sceneActionCmdClass(Data,actionTemp)
        #     action.append(actionTemp)
        #     actionTemp = {}
        # sceneTemp["actions"] = action
        # action=[]
        sceneList.append(sceneTemp)
        sceneTemp = {}
    return sceneList