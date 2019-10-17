import socket
import pickle
import atexit
import random
import sys
import os
from Combat import *
from Classes import *

@atexit.register
def exit():
    host = "127.0.0.1"
    port = 5050
    portc = 4579
    hostc = "127.0.0.1"
    d = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    d.sendto(pickle.dumps((["Disconnect"], [hostname, host, port])), (host, portc))
    s.close()
    s1.shutdown()

def Battle(x, y):
    #if x == "1":
    global dmg1
    dmg1 = Online_Combat(Player1, Player2, x)
    Player2.health -= dmg1
    #if y == "1":
    global dmg2
    dmg2 = Online_Combat(Player2, Player1, y)
    Player1.health -= dmg2
    if Player1.health <= 0:
        global win2
        win2 = 1
        global win1
        win1 = 2
    elif Player2.health <= 0:
	    global win2
	    win2 = 2
	    global win1
	    win1 = 1 


def main():
    host = "127.0.0.1"
    port = 5050
    portc = 4579
    hostc = "127.0.0.1"
    
    global win1
    win1 = 0
    global win2
    win2 = 0
    
    global hostname
    print "what do you want to call your game?"
    option = raw_input(">>> ")
    hostname = option
    os.system('clear')
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto(pickle.dumps([hostname, host, port]), (host, portc))
    global s1
    s1 = socket.socket()
    s1.bind((host, port))
    print "listening for connections"
    s1.listen(1)
    c1, addr1 = s1.accept()
    print "Connection from: " + str(addr1)
    s1.listen(1)
    c2, addr2 = s1.accept()
    print "Connection from: " + str(addr2)
    s1.close()
    s.sendto(pickle.dumps((["Full"], [hostname, host, port])), (host, portc))
    
    data1 = c1.recv(1024)
    global Player1
    Player1 = pickle.loads(data1)
    data2 = c2.recv(1024)
    global Player2
    Player2 = pickle.loads(data2)
    c1.send(data2)
    c2.send(data1)
	
    disconnect = False
    while True:
	    data1 = c1.recv(1024)
	    data2 = c2.recv(1024)
	    if data1 == "Disconnect":
	        c2.send(data1)
	        disconnect = True
	    elif data2 == "Disconnect":
	        c1.send(data2)
	        disconnect = True
	    if disconnect == True:
	        c1.close()  
	        c2.close()
	        s.close()
	        addr1.close()   
	        addr2.close()
	        sys.exit()
	    Battle(data1, data2)
	    Health1 = Player1.health
	    Health2 = Player2.health
	    THealth1 = pickle.dumps([Health1, Health2, win1])
	    THealth2 = pickle.dumps([Health2, Health1, win2])
	    c1.send(THealth1)
	    c2.send(THealth2)
	    if win1 or win2 == "1":
	        sys.exit()
    c1.close()
    c2.close()


    
if __name__ == "__main__":
    main()