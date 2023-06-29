import json


class PayloadCollection:
    username = 'AdminBST'
    password = '3018ZfE1974!3018'
    headers = {'Content-Type': 'application/json'}
    rpcServerUrl =  "http://admin:3018Bern!@31.24.10.138:8332/rpc/"
    wsServerUrl = "ws://admin:3018Bern!@31.24.10.138:8332"
    wsServerCannerald = 'ws://AdminBST:3018ZfE1974!3018@werk-fraubrunnen.onlinezuko.ch//ws?x-ws-token=24b49efff7d447a6aa2b2fa39c33a1fe688e9c642317000a'
    urlControllerServer = "ws://127.0.0.1:5050"
    glutzServerIp = "admin:admin@31.24.10.138"
    glutzServerPort = 8332
    controllerServerIp = "172.20.48.1"
    controllerServerPort = 5050
    connections = [wsServerUrl, urlControllerServer]
    canneraldRpcServerUrl = "https://AdminBST:3018ZfE1974!3018@werk-fraubrunnen.onlinezuko.ch/rpc/"
    lagerHausRpcServerUrl = "https://AdminBST:3018ZfE1974!3018@lagerhausweg-10.onlinezuko.ch/rpc/"

    message = {
        "method": "registerObserver",
        "params": [
            [
                "UsersGroups",
                "UserGroupRelations",
                "Codes",
                "Media",
                "Devices",
                "AccessPoints",
                "AuthorizationPoints",
                "AuthorizationPointRelations",
                "DeviceEvents",
                "Rights",
                "ObservedStates",
                "TimeProfiles",
                "TimeSlots",
                "DeviceStatus",
                "RouteTree",
                "Properties",
                "PropertyValueSpecs",
                "DevicePropertyData",
                "DeviceStaticPropertyData",
                "SystemPropertyData",
                "AccessPointPropertyData",
                "UserPropertyData",
                "HolidayCalendars",
                "Holidays",
                "DeviceUpdates",
                "EventLog",
                "CustomProperties",
                "Logins",
                "ActionProfiles",
                "PermissionProfiles",
                "Permissions",
                "Subsystems",
                "CustomFilesTree",
            ]
        ],
        "jsonrpc": "2.0",
    }
    userGroupRelations = json.dumps(
        {
            "method": "eAccess.getModel",
            "params": ["UserGroupRelations", {}, []],
            "id": 16,
            "jsonrpc": "2.0",
        }
    )
    authorizationPointId = json.dumps(
        {
            "method": "eAccess.getModel",
            "params": [
                "Rights",
                {},
                [
                    "id",
                    "userId",
                    "authorizationPointId",
                    "timeProfileId",
                    "validFrom",
                    "validTo",
                    "actions",
                    "options",
                ],
            ],
            "id": 16,
            "jsonrpc": "2.0",
        }
    )
    usersGroups = json.dumps(
        {
            "method": "eAccess.getModel",
            "params": ["UsersGroups", {}, ["id", "subsystemId", "label", "class"]],
            "id": 6,
            "jsonrpc": "2.0",
        }
    )
    devices = json.dumps(
        {
            "method": "eAccess.getModel",
            "params": [
                "Devices",
                {},
                ["id", "label", "deviceid", "deviceType", "accessPointId", "roles"],
            ],
            "id": 8,
            "jsonrpc": "2.0",
        }
    )
    accessPointPropertyData = json.dumps(
        {
            "method": "eAccess.getModel",
            "params": ["AccessPointPropertyData", {}, []],
            "id": 2,
            "jsonrpc": "2.0",
        }
    )
    accessPoints = json.dumps(
        {
            "method": "eAccess.getModel",
            "params": ["AccessPoints", {}, ["id", "label", "function"]],
            "id": 8,
            "jsonrpc": "2.0",
        }
    )

    @staticmethod
    def addAcceccPointToUser(userId, authorizationPointId, validTo):
        payLoad = json.dumps(
            {
                "method": "eAccess.setModel",
                "params": [
                    "Rights",
                    {
                        "userId": userId,
                        "authorizationPointId": authorizationPointId,
                        "actions": None,
                        "timeProfileId": None,
                        "validFrom": None,
                        "validTo": validTo,
                        "options": None,
                    },
                ],
                "id": 23,
                "jsonrpc": "2.0",
            }
        )
        return payLoad

    @staticmethod
    def getAccessPoint():
        payload = json.dumps(
            {
                "method": "eAccess.getModel",
                "params": [
                    "Rights",
                    {},
                    [
                        "id",
                        "userId",
                        "authorizationPointId",
                        "timeProfileId",
                        "validFrom",
                        "validTo",
                        "actions",
                        "options",
                    ],
                ],
                "id": 16,
                "jsonrpc": "2.0",
            }
        )
        return payload

    @staticmethod
    def deleteOldAccessPoint(id):
        payload = json.dumps(
            {
                "method": "eAccess.setModel",
                "params": ["Rights", {"id": id}],
                "id": 23,
                "jsonrpc": "2.0",
            }
        )
        return payload

    @staticmethod
    def searchUserIdByMediaId():
        payload = json.dumps(
            {
                "method": "eAccess.getModel",
                "params": [
                    "Media",
                    {},
                    [
                        "id",
                        "userId",
                        "publicMediaLabel",
                    ],
                ],
                "id": 7,
                "jsonrpc": "2.0",
            }
        )
        return payload
    accessPointsWith2FactorAuthList = ['BS1']

