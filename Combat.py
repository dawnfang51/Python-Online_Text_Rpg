import random
from Items import *
from Classes import *


def Online_Combat(AtkPlayer, DefPlayer, skill):
    if skill != "melee" and skill != "magic" and skill != "range":
        #if skill != 0:
        if AtkPlayer.skilltree[skill][4] == 0:
            return random.randint(int(AtkPlayer.skilltree[skill][0]/3), int(AtkPlayer.skilltree[skill][0]))
        elif AtkPlayer.skilltree[skill][4] == 1:
            """
            while target != "ally" or target != "self":
                print "Do you want to target yourself or ally?"
                print "1.) Self"
                print "2.) Ally"
                if target == "1":
                    target = "self"
                elif target == "2":
                    target = "ally"
                target = raw_input('>>> ')
            target.health += skill(1)
            """
            PlayerIG.health += AtkPlayer.skilltree[skill][1]
        #elif skill(4) == 2:
        #    PlayerIG.health += skill(1)
    elif skill == "melee":
        return random.randint(int(AtkPlayer.attack)/3, AtkPlayer.attack)
    elif skill == "magic":
        pass
    else:
        pass
        #return random.randint(int(AtkPlayer.attack/3), AtkPlayer.attack)
    

#target = 3 && 4
#damage = 0
