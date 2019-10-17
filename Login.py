import hashlib
import socket
import pickle 
import time
import psycopg2
from Classes import Player
from Items import *

global host
global port
host = "127.0.0.1"
port = 7788



class user:
    def __init__(self, name, password, email):
        self.name = name
        self.password = password
        self.email = email

def main():
    print "What do you want to do?"
    print "1.) Register"
    print "2.) Login"
    option = raw_input(">>> ")
    if option == "1":
        register()
    elif option == "2":
        login()
    else:
        main()
        
def register():
    print "What do you want your username to be?"
    option = raw_input(">>> ")
    name = option
    print "What is your email?"
    option = raw_input(">>> ")
    email = option
    while True:
        print "What do you want your password to be?"
        option = raw_input(">>> ")
        password = option
        print "Confirm password"
        option = raw_input(">>> ")
        if option != password:
            print "passwords do not match."
        elif len(option) < 6:
            print "password must be at least 6 characters long."
        else:
            password = hashlib.sha224(password).hexdigest()
            break
    PlayerIG = Player(name, ("Mage", Classes["Mage".title()]))
    command = """
    INSERT INTO users VALUES
        (%s, %s, %s, %s, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %s, %s, %s, %s, %s, %d %s, %s )
    """ % (PlayerIG.name, PlayerIG.cclass, PlayerIG.skilltree, PlayerIG.skills, PlayerIG.max_mana, PlayerIG.max_health, PlayerIG.max_stamina, PlayerIG.stamina, PlayerIG.health, PlayerIG.mana, PlayerIG.attack, PlayerIG.strength, PlayerIG.intelligence, PlayerIG.endurance, PlayerIG.base_speed, PlayerIG.boots, PlayerIG.weap, PlayerIG.armor, PlayerIG.helm, PlayerIG.misc, PlayerIG.arrows, email, password)
    conn = psycopg2.connect("dbname=rpg user=postgres password=password")
    cur = conn.cursor()
    cur.execute(command)
    print "user successfully created"
    
def login():
    print "Username: "
    username = raw_input(">>> ")
    print "Password: "
    password = raw_input(">>> ")
    password = hashlib.sha224(password).hexdigest()
    User = [username, password]
    UserObj = pickle.dumps(User)
    s = socket.socket()
    s.connect((host, port))
    print "connected"
    s.send("login")
    time.sleep(1)
    s.send(UserObj)
    success = s.recv(100)
    print success
    
if __name__ == "__main__":
    main()