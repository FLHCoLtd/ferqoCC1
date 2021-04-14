import random, string
class scene():
    def __init__(self, gatewayInfo):
        requestId = "FLH-" + ''.join(random.choice(string.ascii_letters + string.digits) for x in range(20))
        self.body = {
                    "requestId": "FLH-11e6b1a064510650abcf",
                    "intent": "action.scene.QUERY"
        }
        self.body["requestId"] = requestId
        payload = {}
        self.body["payload"] = payload
        self.body["payload"]["gateway_id"] = gatewayInfo["gateway_id"]
        self.body["payload"]["account"] = gatewayInfo["account"]
        self.body["payload"]["password"] = gatewayInfo["password"]
    def sceneAction(self, sceneid):
        self.body["payload"]["sceneid"] = sceneid
        self.body["intent"] = "action.scene.EXECUTE"
        self.body["payload"]["action"] = "true"