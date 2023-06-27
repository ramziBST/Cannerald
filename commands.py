import json

import requests

from payloadCollection import PayloadCollection


class Command:
    def __init__(self):
        self.serverUrl = PayloadCollection.serverUrl
        self.headers = PayloadCollection.headers
        self.accessPointsWith2FactorAuthList = PayloadCollection.accessPointsWith2FactorAuthList

    @staticmethod
    def activateOutput(deviceId, outputNum):
        return

    def getAccessPointsWith2FactorAuth(self):
        response = requests.request("POST", self.serverUrl, headers=self.headers,
                                    data=PayloadCollection.accessPoints)
        results = json.loads(response.text)['result']
        print(results)

        for result in results:
            if result['label'] in self.accessPointsWith2FactorAuthList:
                print(result['label'])
                #groupId = result['id']

            #return groupId
    def getAccessPointsPropertyData(self):
        response = requests.request("POST",self.serverUrl,headers=self.headers,
                                    data=PayloadCollection.accessPointPropertyData)
        results = json.loads(response.text)['result']
        print(results)




command = Command()
command.getAccessPointsPropertyData()
