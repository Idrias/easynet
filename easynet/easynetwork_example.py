#!/usr/bin/python3

import easyclient # when easyclient is in same folder, otherwise easynet.easyclient
import easyserver # same as above
import time

myserver = easyserver.Server("localhost", 1337)
myserver.start()

myclient = easyclient.Client("localhost", 1336, "localhost", 1337)
myclient.start()

time.sleep(0.1)
myclient.send(b'Hello Server!')
myserver.sendall(b"Hello Client!")

myserver.ping(5, 0.2)
time.sleep(0.1)
myserver.showpings()

time.sleep(0.1)
print("The client has a new message:", myclient.datalist[0])
print("The server has a new message:", myserver.datalist[0].text, "from", myserver.datalist[0].sender)
time.sleep(10)

