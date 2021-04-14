def HAType(deviceList):
    HADeviceList = {}
    sensor = []
    light = []
    switch = []
    cover = []
    ir = []
    lock = [] 
    scene_controller = []
    temp = {}
    HADeviceList["sensor"] = sensor
    HADeviceList["light"] = light
    HADeviceList["switch"] = switch
    HADeviceList["cover"] = cover
    HADeviceList["scene controller"] = scene_controller
    HADeviceList["lock"] = lock
    HADeviceList["ir"] = ir
    for i in range(len(deviceList)):
        temp = deviceList[i]
        if (deviceList[i]["HAtype"] == "sensor"):
            sensor.append(temp)
        elif (deviceList[i]["HAtype"] == "switch"):
            switch.append(temp)
        elif (deviceList[i]["HAtype"] == "light"):
            light.append(temp)
        elif (deviceList[i]["HAtype"] == "cover"):
            cover.append(temp)
        elif (deviceList[i]["HAtype"] == "lock"):
            lock.append(temp)
        elif (deviceList[i]["HAtype"] == "scene controller"):
            scene_controller.append(temp)
        elif (deviceList[i]["HAtype"] == "ir"):
            ir.append(temp)
        temp = {}
    return HADeviceList
def SensorValueSplit(sensorList):
    newSensorList = []
    tempListT = []
    tempList = {}
    temp = []
    for i in range(len(sensorList)):
        tempList = sensorList[i].pop("sensorValue")
        for j in range(len(tempList)):
            tempList[j].update(sensorList[i])
        tempListT.append(tempList)

    for i in range(len(tempListT)):
        temp = temp + tempListT[i]
    newSensorList = temp
    return newSensorList
def MutichannelValueSplit(multiList):
    newList = []
    lightList = []
    multiDeviceList = []
    tempListT = []
    tempList = {}
    temp = []
    temp2 = []
    for i in range(len(multiList)):
        if "multiChannel" in multiList[i]:
            if multiList[i]["subType"] != "multilevel":
                tempList = multiList[i].pop("multiChannel")
                if "status" in multiList[i]:
                    trash = multiList[i].pop("status")
                for j in range(len(tempList)):
                    if "signal" in tempList[j]:
                        if (tempList[j]["signal"] == "output"):
                            tempList[j].update(multiList[i])
                        else:
                            pass
                    else:
                        pass
                tempListT.append(tempList)
            else:
                lightList.append(multiList[i])
        else:
            lightList.append(multiList[i])
    for i in range(len(tempListT)):
        temp = temp + tempListT[i]
    for i in range(len(temp)):
        if "signal" in temp[i]:
            multiDeviceList.append(temp[i])
        else:
            pass
    temp2.append(lightList)
    temp2.append(multiDeviceList)
    for i in range(len(temp2)):
        newList = newList + temp2[i]
    return newList

