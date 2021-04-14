import json

def cToF(C):
    F = (C * 9 / 5) + 32
    return F
def fToC(F):
    C = ( F - 32 ) * 5 / 9
    return C
def hexToDec(hexNum):
    H2D_num = int(hexNum, 16)
    return H2D_num
def decToHex(decNum):
    D2H_num = hex(decNum).split('x')[1]
    if (decNum < 16):
        D2H_num = "0" + str(D2H_num)
    return D2H_num
def decToBin(decNum):
    D2B_num = bin(decNum).split("b")[1]
    for i in range(8-len(D2B_num)):
        D2B_num = "0" + D2B_num
    return D2B_num
def binToDec(binNum):
    B2D_num = int(binNum, 2)
    return B2D_num
def calculateParameter(parameter2,parameter3):
    D2HTemp1 = decToHex(parameter2)
    D2HTemp2 = decToHex(parameter3)
    H2Dtemp = str(D2HTemp1) + str(D2HTemp2)
    return H2Dtemp
def serchDevice(deviceInfoData,eventData):
    for i in range(len(deviceInfoData)):
        if (deviceInfoData[i]["node_id"] == eventData["node_id"]):
            eventData["type"] = deviceInfoData[i]["type"]