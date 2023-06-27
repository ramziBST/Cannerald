import asyncio
import websockets.exceptions
from websockets import connect
import time
from datetime import datetime
from observer import Observer
from payloadCollection import *


async def listen(url):
    counter = 1

    while counter < 500000:
        try:
            async with connect(url) as websocket:
                if url == PayloadCollection.urlGlutzServer:

                    await websocket.send(json.dumps(PayloadCollection.message))
                    print('Hoi We are Connected  to Glutz Server')
                    counter = 1
                    while True:
                        msg = await websocket.recv()
                        params = json.loads(msg)['params']
                        observer = Observer()
                        observer.observer(params=params)



        except ConnectionRefusedError:
            print(f"Hoi We don't have connection Please control the {url} Server  ")
            time.sleep(1)
            print(f'I am trying to reconnet for the {counter} time ')
            counter += 1

        except (websockets.exceptions.ConnectionClosedOK, websockets.exceptions.ConnectionClosedError):
            print(f'Hoi We lost connection Please control the Internet   {url}')
            time.sleep(1)
            print(f'I am trying to reconnect for the {counter} time ')
            counter += 1

        except OSError:
            time.sleep(1)

            print(f'No internet Connection and i will try to  reconnect for the {counter} time ')
            counter += 1
        except asyncio.exceptions.TimeoutError:
            time.sleep(1)
            counter += 1
        except websockets.ConnectionClosed:
            continue


async def serversHandler():
    try:
        task_Glutz = asyncio.create_task(listen( PayloadCollection.urlGlutzServer))
        # task_ControllerServer = asyncio.create_task(listen(urlControllerServer))
        await asyncio.wait([task_Glutz])
        # await asyncio.wait([listen(uri) for uri in connections])
    except OSError as e:
        print(f'this {e}')


asyncio.run(serversHandler())
