#from Crypto.Cipher import AES
#from Crypto.PublicKey import RSA
#from Crypto import Random
import binascii
import base64
import socket
import os
import random
import sys
import pickle
import subprocess
import time
import atexit
from Login import *
from Items import *
from Classes import *

@atexit.register
def exit():
	if MP_Game == True:
		s2.send("Disconnect")

def Main():
	os.system("clear")
	print "What do you want to do?\n"
	print "1.) Start"
	print "2.) Load"
	print "3.) Quit"
	option = raw_input("-> ")
	if option == "1":
		startp()
	elif option == "3":
		sys.exit()
	elif option == "2":
		if os.path.exists("savefile") == True:
			os.system('clear')
			with open('x5213', 'rb') as c:
				cipher = pickle.load(c)
			with open('savefile', 'rb') as f:
				global PlayerIG
				PlayerIG = cipher.decrypt(base64.b64decode(pickle.load(f)))
			print "Loaded last save state..."
			option = raw_input(" ")
			Start()
	else:
		Main()

######################
# Creation of Player #
######################

def startp():
	os.system('clear')
	while True:
		os.system('clear')
		print "What race are you?"
		print "- Race determines beginning stats"
		print ""
		for race in Races:
			print "%s: \tstrength: %i  intelligence: %i  dexterity: %i  vitality: %i" % (race, Races[race][0], Races[race][1], Races[race][2], Races[race][3])
		option = raw_input('>>> ')
		if option.title() in Races:
			race = option.title()
			break
	os.system('clear')
	while True:
		os.system('clear')
		print "What class are you?\n"
		print "- Classes determine skills"
		for cclass in Classes:
			print cclass
		option = raw_input(">>> ")
		if option.title() in Classes:
			cclass = (option, Classes[option.title()])
			break
	os.system('clear')
	print ("What is your name?")
	option = raw_input("-> ")
	
	if len(option) < 1:
		startp()
		
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	#~ Giving Player Beginning Stats~
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	
	else:
		global PlayerIG
		PlayerIG = Player(option, cclass)
		PlayerIG.race = race
		for key in PlayerIG.cclass[1]:
			if key != PlayerIG.cclass[1][4]:
				PlayerIG.inventory.append(key)
				if key in Armor_Stat_List:
					PlayerIG.armor = key
				elif key in Weapons_Stat_List:
					PlayerIG.weap = key
				elif key in Boot_Stat_List:
					PlayerIG.boots = key
				else:
					PlayerIG.helm = key
		PlayerIG.base_strength = Races[PlayerIG.race][0]
		PlayerIG.base_intelligence = Races[PlayerIG.race][1]
		PlayerIG.base_dexterity = Races[PlayerIG.race][2]
		PlayerIG.base_vitality = Races[PlayerIG.race][3]
		
		for ability in PlayerIG.skilltree:
			if PlayerIG.skilltree[ability][5] == 1:
				PlayerIG.skills.append(ability)
		Start()



def Start():
	os.system('clear')
	print "==__===============================__=="
	print "=\tWhat do you want to do?"
	print "=\t1.) Multiplayer"
	print "=\t2.) View Abilities"
	print "=\t3.) Save"
	print "=\t4.) Exit"
	print "==__===============================__=="
	option = raw_input("-> ")
	if option == "1":
		MP_Join()
	elif option == "2":
		AbilityPrint(PlayerIG.skilltree)
		option = raw_input(" ")
		Start()
	elif option == "4":
		sys.exit()
	elif option == "3":
		os.system('clear')
		with open('x5213', 'wb') as c:
			#rng = Random.new().read
			#RSAkey = RSA.generate(1024, rng) 
			iv = os.urandom(16)
			obj = AES.new("00112233445566778899aabbccddeeff", AES.MODE_CBC, iv) 
			cipher = obj.encrypt("asdf123456789012")
			print cipher
			option = raw_input("  ")
			pickle.dump(cipher, c)
		with open('savefile', 'wb') as f:
			data = pickle.dump(PlayerIG)
			f.write(base64.b64encode(cipher.encrypt(data)))
		print "\nGame has been saved...\n"
		option = raw_input(" ")
		Start()
	else:
		Start()




##########################################################
################# MULTIPLAYER ############################
##########################################################


def connect(host, port, s):
    s.connect((host, port))
    global data
    data = pickle.loads(s.recv(1024))


def MP_Join():
    host = "127.0.0.1"
    port = 4579
    serverup = True

    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    global s1
    s1 = socket.socket()
    global s2
    s2 = socket.socket()
    s.sendto("Connect", (host, port))
    time.sleep(1)
    try:
        connect(host, port, s1)
    except:
    	print "Failed to connect to main server..."
    	option = raw_input(' ')
    	Start()
    
    while serverup == True:
        os.system('clear')
        s1.close()
        print "="*35
        print "         Server List:"
        print "="*35
        for server in data:
            if len(server) == 4:
                print "%s : %s : %s" % (server[0], server[1], server[3])
            else:
                print "%s : %s " % (server[0], server[1])
        print "what do you want to connect to?"
        print "type \"r\" to refresh or \"b\" to go back"
        option = raw_input(" ")
        if option.lower() == "r":
        	MP_Join()
    	elif option.lower() == "b":
    		Start()
    	else:
	        for server in data:
	            if option == server[0]:
	               	try:
	                   	s2.connect((server[1], server[2]))
	               	except:
	               		os.system('clear')
	                   	print "Failed to connect."
	                   	print "Server is either offline or full"
	                   	option = raw_input(' ')
	                   	MP_Join()
	               	print "connected!"
	               	serverup = False
			print "Waiting for other player to connect."
			PlayerObj = pickle.dumps(PlayerIG)
			try:
				s2.send(PlayerObj)
				global MP_Game
				MP_Game = True
				global MP_Enemy
				MP_Enemy = s2.recv(1024)
				MP_Enemy = pickle.loads(MP_Enemy)
			except:
				print "Server has disconnected"
				option = raw_input(" ")
				s.close()
				s2.close()
				Start()
			while True:
				Mp_PvPFormat(MP_Enemy.name, MP_Enemy.health)
				try:
					s2.send(mpinput)
					os.system('clear')
					print "Waiting for other player to respond..."
					Damage = s2.recv(1024)
					Damage = pickle.loads(Damage)
				except:
					print "Server has disconnected"
					option = raw_input(" ")
					s.close()
					s2.close()
					Start()
					
				if Damage == "Disconnect":
					print "Enemy has disconnected"
					option = raw_input(" ")
					s.close()
					s2.close()
					Start()
				Damage_Dealt(PlayerIG.health-Damage[0], MP_Enemy.health-Damage[1])
				PlayerIG.health = Damage[0]
				MP_Enemy.health = Damage[1]
				if Damage[2] != 0:
					if Damage[2] == 1:
						mp_win()
					elif Damage[2] == 2:
						mp_lose()



def Mp_PvPFormat(name, health):
	os.system('clear')
	print "================================"
	print "|%s vs %s"  % (PlayerIG.name, name)
	print "|==============================="
	print "|%s Health: %i" % (name, health)
	print "|%s Health: %i" % (PlayerIG.name, PlayerIG.health)
	print "================================"
	print "| 1.) Attack"
	print "| 2.) Use Ability"
	print "| 3.) Surrender"
	print "================================"
	global mpinput
	mpinput = raw_input("->")
	
	if mpinput == "1":
		while True:
			os.system('clear')
			print "What type of attack do you want to perform"
			print "1.) Melee"
			print "2.) Magic"
			print "3.) Range (costs an arrow)"
			print "b.) Go back"
			mpinput = raw_input("->")
			if mpinput == "1":
				mpinput = "melee"
				break
			elif mpinput == "2":
				mpinput = "magic"
				break
			elif mpinput == "3":
				if PlayerIG.arrows >= 1:
					mpinput = "range"
					break
				else:
					os.system('clear')
					print "You don't have any arrows."
					option = raw_input(' ')
			elif mpinput == "b" or mpinput == "B":
				Mp_PvPFormat(name, health)
	
	elif mpinput == "2":
		os.system('clear')
		AbilityPrint(PlayerIG.skilltree)
		print "What ability do you want to use?"
		print "b.) Go back"
		option = raw_input(">>> ")
		if option.title() in PlayerIG.skilltree:
			print "You used %s!" % option
			mpinput = option.title()
		elif option == "b" or option == "B":
			Mp_PvPFormat(name, health)
		else: 
			print "You don't have that skill"
			option = raw_input(" ")
			Mp_PvPFormat(name, health)
			
	else: 
		Mp_PvPFormat(name, health)
			

def Damage_Dealt(x, y):
	os.system('clear')
	print "You take %i damage" % x
	print "You deal %i damage to %s" % (y, MP_Enemy.name)
	option = raw_input(' ')


def mp_win():
	print "Congratulations you have defeated %s" % MP_Enemy.name
	option = raw_input(' ')
	s.close()
	s2.close()
	Start()


def mp_lose():
	print "You have lost against %s" % MP_Enemy.name
	option = raw_input(' ')
	s.close()
	s2.close()
	Start()

######################
# END Of MULTIPLAYER #
######################

if __name__ == '__main__':
	Main()


