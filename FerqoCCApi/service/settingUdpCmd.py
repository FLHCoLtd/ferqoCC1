import random
#Query all device
Zwave_node_all_info = 206 #all Query
Zwave_node_info = 207 #one Query
Zwave_node_sned_data = 202 #Execute cmd
Zwave_scene_get_all_info = 227
Zwave_scene_get_info = 226
def settingCMD(gatewayAuth,node_id = "none"):
    data = []
    user = gatewayAuth["account"]
    password = gatewayAuth["password"]
    intent = gatewayAuth["body"]["intent"]
    data.insert(0,0)  # "reserved"
    data.insert(1,0)  #"dataLen":this is ignored, not used
    data.insert(2,random.randrange(1,100))  #"seq_no":the response packet must copy this byte back
    if (str(intent.split(".")[2]) == "QUERY"):
        data.insert(3,63)#"opcode"  defined in LOCAL_SDK_OP_E
    elif (str(intent.split(".")[2]) == "EXECUTE"):
        data.insert(3,60)#"opcode"  defined in LOCAL_SDK_OP_E
    data.insert(4,1)  #"version":version = 1
    data.insert(5,136)  #"magic_id":from gateway : 0x77, from App : 0x88
    data.insert(6,int(gatewayAuth["gateway_id"][0] + gatewayAuth["gateway_id"][1] + gatewayAuth["gateway_id"][2]) - 1)
    data.insert(7,int(gatewayAuth["gateway_id"][3] + gatewayAuth["gateway_id"][4] + gatewayAuth["gateway_id"][5]) - 1)
    data.insert(8,int(gatewayAuth["gateway_id"][6] + gatewayAuth["gateway_id"][7] + gatewayAuth["gateway_id"][8]) - 1)
    data.insert(9, 0)
    data.insert(10,0)
    data.insert(11,0)
    data.insert(12,1)# random id of App, changed for each
    userLen = len(gatewayAuth["account"])
    for i in range(13,33):
        if (i < userLen + 13):
            data.insert (i, ord(gatewayAuth["account"][i-13]))
        else:
            data.insert(i, 0)
    passwordLen = len(gatewayAuth["password"])
    for i in range(33,53):
        if (i < userLen + 33):
            data.insert(i, ord(gatewayAuth["password"][i-33]))
        else:
            data.insert(i, 0)
    data.insert(53,int(gatewayAuth["App_ip"].split(".",4)[0]))
    data.insert(54,int(gatewayAuth["App_ip"].split(".",4)[1]))
    data.insert(55,int(gatewayAuth["App_ip"].split(".",4)[2]))
    data.insert(56,int(gatewayAuth["App_ip"].split(".",4)[3]))# app_ip[4]  # ip address of the App
    data.insert(57,43)
    data.insert(58,48)# app_port[2]  # App port
    data.insert(59,0)
    data.insert(60,0)
    data.insert(61,0)
    data.insert(62,0)# reserved_for_gw[4] 
    data.insert(63,0)#fail_code
    #tlv_size
    if (str(intent.split(".")[2]) == "QUERY"):
        data.insert(64,0) 
        data.insert(65,0) 
        data.insert(66,0)
        data.insert(67,8)
    elif (str(intent.split(".")[2]) == "EXECUTE"):
        settingLen = gatewayAuth["body"]["payload"]["command"]["cmdLen"]
        data.insert(64,0) 
        data.insert(65,0) 
        data.insert(66,0)
        data.insert(67,settingLen+6)
    #tlv_type
    if (intent.split(".")[1] == "device"):
        if (str(intent.split(".")[2]) == "QUERY"):
            if (node_id == "none"):
                data.insert(68,0)
                data.insert(69,207)
            else:
                data.insert(68,0)
                data.insert(69,206)
        elif (str(intent.split(".")[2]) == "EXECUTE"):
            data.insert(68,0)
            data.insert(69,202)
    elif (intent.split(".")[2] == "scene"):
        if (node_id == "none"):
            data.insert(68,0)
            data.insert(69,227)
        else:
            data.insert(68,0)
            data.insert(69,226)
    #setting_len
    if (str(intent.split(".")[2]) == "QUERY"):
        data.insert(70,0)
        data.insert(71,4)
        #settings
        data.insert(72,0) 
        data.insert(73,0) 
        data.insert(74,0)
        if (node_id == "none"):
            data.insert(75,0)
        else:
            for i in range(len(gatewayAuth["deviceList"])):
                if ( gatewayAuth["deviceList"][i]["node_id"] == node_id):
                    deviceNumber = gatewayAuth["deviceList"][i]["seq_number"]
                    data.insert(75,int(deviceNumber))
                else:
                    pass
        data.insert(76,0)# empty  # set to 0
        data.insert(77,0)# checksum  # not used
    elif (str(intent.split(".")[2]) == "EXECUTE"):
        data.insert(70,0)
        settingLen = gatewayAuth["body"]["payload"]["command"]["cmdLen"]
        data.insert(71,settingLen+2)
        data.insert(72,gatewayAuth["body"]["payload"]["nodeid"])
        data.insert(73,gatewayAuth["body"]["payload"]["command"]["cmdLen"])
        data.insert(74,gatewayAuth["body"]["payload"]["command"]["cmd_class"])
        data.insert(75,gatewayAuth["body"]["payload"]["command"]["cmd"])
        for i in range(settingLen-2):
            data.insert(76+i,gatewayAuth["body"]["payload"]["command"]["parameters"][str(i)])
        data.insert(76+settingLen-2,0)# empty  # set to 0
        data.insert(77+settingLen-2,0)# checksum  # not used
    #settings
    return data
def sysncDeviceNumber(gatewayAuth,data):
    for i in range(len(gatewayAuth["deviceList"])):
        if ( gatewayAuth["deviceList"][i]["node_id"] == data[0]["node_id"]):
            data[0]["seq_number"] = gatewayAuth["deviceList"][i]["seq_number"]
        else:
            pass
    return data
