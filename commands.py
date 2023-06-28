import json
import requests
from payloadCollection import PayloadCollection
from requests.auth import HTTPBasicAuth

class Command:
    def __init__(self):
        self.serverUrl = PayloadCollection.rpcServerUrl
        self.canneraldRpc = PayloadCollection.canneraldRpcServerUrl
        self.lagerhausRpc = PayloadCollection.lagerHausRpcServerUrl
        self.headers = PayloadCollection.headers
        self.accessPointsWith2FactorAuthList = PayloadCollection.accessPointsWith2FactorAuthList

    @staticmethod
    def activateOutput(deviceId, outputNum):
        return

    def getAccessPointsWith2FactorAuth(self):
        response = requests.get("POST", self.serverUrl, headers=self.headers,verify=True,
                                    data=PayloadCollection.accessPoints)
        results = json.loads(response.text)['result']
        print(results)

        for result in results:
            if result['label'] in self.accessPointsWith2FactorAuthList:
                print(result['label'])
                #groupId = result['id']

            #return groupId
    def getAccessPointsPropertyData(self):
        url = 'https://AdminBST:3018ZfE1974!3018@werk-fraubrunnen.onlinezuko.ch/rpc/'
        response = requests.get(url= url, headers=self.headers,verify=False,
                                    data=PayloadCollection.accessPointPropertyData )




        results = json.loads(response.text)['result']
        #print(results)
        for result in results:
            print(result)


commond = Command()
commond.getAccessPointsPropertyData()
