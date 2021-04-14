import select, socket

#import numpy as np
def udpConnect(ip, port, Cmd):
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    server.bind(('', 0))
    server.sendto(Cmd, (ip, port))
    sendIp , sendPort = server.getsockname()
    print('Listening for broadcast at ', server.getsockname())
    print("message sent!", flush=True)
    data = server.recvfrom(65535)
    print('Server received from :{}'.format(data))
    return data
def udpBroadcast(gatewayAuth):
    response = {}
    serchGW = bytes([0, 255, 138, 1, 1, 136, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0])
    ip = '<broadcast>'
    port = 11188
    data, addr = udpConnect(ip, port, serchGW)
    response["data"] = data
    gw = np.array(addr)
    gatewayAuth["App_ip"] = get_host_ip()
    response["gateway_id"] = str(data[6]+1).zfill(3) + str(data[7]+1).zfill(3) + str(data[8]+1).zfill(3)
    if (gatewayAuth["gateway_id"] == response["gateway_id"]):
        gatewayAuth["gateway_ip"] = str(gw[0])
        gatewayAuth["gateway_port"] = int(gw[1])
    else:
        gatewayAuth["error_code"] = "can not find gateway"
    return gatewayAuth
def udpSend(gatewayAuth,Cmd):
    ip = gatewayAuth["gateway_ip"]
    port = gatewayAuth["gateway_port"]
    data,addr = udpConnect(ip, port, Cmd)
    # for i in range(len(data)):
    #     string = str(i) + " :" + str(data[i])
    #     print( string )
    # print(len(data))
    #data = InfoAnalytics(data,"response")
    return data
def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip