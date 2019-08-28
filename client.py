import websocket
try:
    import thread
except ImportError:
    import _thread as thread
import time
import json
import runpy
from Scripts import test
from Scripts import colors
from Scripts import distance

server_adress = "ws://192.168.33.109/ws/test"


def on_message(ws, message):
    message = json.loads(message)
    beginTime = time.time()
    #print(message['type'])
    if message['type'] == "is_ready":
        print("Board is ready")
        #data_result = "OK"
        #data_type = "is_ready"
    elif message['type'] == "timeout":
        print("Timeout")
        #ws.close()
        #data_type = "timeout"
    elif message['type'] == "init_module":
        module = message['message']
        win = module['win_condition']
        data_result = {}
        if module['type'] == "distance":
            print("distance")
            #data_result["status"] = test.start(win)
        elif module['type'] == "colors":
            print("colors")
            #data_result["status"] = colors.start(win)
        elif module['type'] == "test":
            data_result["status"] = test.start()
            #print(data_result)
        data_result['position'] = module['position']
        data_type = "end_module"

        if time.time() < beginTime + module['time_max']:
            result = {}
            result['sender'] = "board"
            result['message'] = data_result
            result['type'] = data_type
            result = json.dumps(result)
            #print(result)

    #ws.send(result)
    #print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        time.sleep(1)
        #ws.close()
    thread.start_new_thread(run, ())


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(server_adress,
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever(ping_interval=10)