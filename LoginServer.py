import socket 
import threading
import pickle
import Classes
import psycopg2

####################

class user:
    def __init__(self, name, password, email):
        self.name = name
        self.password = password
        self.email = email

def register(c):
    userdata = c.recv(1024)
    userdata = pickle.loads(userdata)
    print userdata
    UserList.append(userdata)
    for u in UserList:
        print u.name

def login(c):
    userdata = c.recv(1024)
    userdata = pickle.loads(userdata)
    login = False
    for u in UserList:
        if u.name == userdata[0] and u.password == userdata[1]:
            c.send("You have successfully logged in as %s" % u.name)
            login = True
            break
    if login == False:
        c.send("Your username or password is incorrect.")
    
        
def main1():
    cnx = mysql.connector.connect(**config)
    

def main():
    host = '127.0.0.1'
    port = 7788
    
    s = socket.socket()
    s.bind((host, port))
    
    while True:
        print "Waiting for Connection"
        s.listen(1)
        c, addr = s.accept()
        print "Connection Recieved"
        logtype = c.recv(100)
        if logtype == "register":
            register(c)
        else:
            login(c)
        
            
            
if __name__ == "__main__":
    threading.Thread(target=main).start()
    