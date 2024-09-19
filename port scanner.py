import socket
import threading
from queue import Queue

print(" ")
print("Simple Portscanner")
print("Warning: this tool must be used only for education or legal pentesting!")
print("Notice: if you leave the input blank, it'll scan the local host.")
target = input("Insert the IP's target: ")
queue = Queue()
openPorts = []


def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False


def fillQueue(portList):
    for port in portList:
        queue.put(port)


def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print("Port {} is open!".format(port))
            openPorts.append(port)

portList = range(1, 65536)
fillQueue(portList)

threadList = []

for t in range(10):
    thread = threading.Thread(target=worker)
    threadList.append(thread)

for thread in threadList:
    thread.start()

for thread in threadList:
    thread.join()

print("Open ports are: ", openPorts)
