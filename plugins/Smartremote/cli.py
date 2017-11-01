#!/usr/bin/env python3

import websocket
import urllib.request
import payloads
import time
from sys import argv, exit

#ip = "192.168.88.156"

def get_key(ip):
    try:
        u = urllib.request.urlopen('http://'+ip+':8000/socket.io/1/')
        s = u.read()
        print(s)
        key = s.split(b':')[0]
        return key.decode('utf-8')
    except:
        print("Error getting connection key")
        raise
    
def connect(ip):
    key = get_key(ip)
    print(key)
    url = "ws://"+ip+':8000/socket.io/1/websocket/'+key
    print(url)
    ws = websocket.WebSocket()
    ws.connect(url)
    #time.sleep(.1)
    for p in payloads.init:
        ws.send(p)
        #time.sleep(.1)
    return ws



if __name__ == '__main__':
    try:
        ip = argv[1]
        command = getattr(payloads, argv[2])
    except (AttributeError, IndexError):
        print("Usage: samsung-client.py [ip] [command]")
        print("Available commands:")
        for c in dir(payloads):
            if (c[0] != '_' and c != 'init'):
                print(c)
        exit()
    ws = connect(ip)
    ws.send(command)
