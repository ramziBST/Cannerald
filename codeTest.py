import jsonrpclib

canneraldRpcServerUrl = "https://AdminBST:3018ZfE1974!3018@werk-fraubrunnen.onlinezuko.ch/rpc/"
lagerHausRpcServerUrl = "https://AdminBST:3018ZfE1974!3018@lagerhausweg-10.onlinezuko.ch/rpc/"



server = jsonrpclib.Server(lagerHausRpcServerUrl)


resp = server.eAccess.getModel('UsersGroups')
print(resp.data)