import os
#Skill Trees

#"Template" : [damage, heal, buff, #_of_targets, target_friend_or_foe_or_self, level, Attack Type]
#0=enemy
#1=ally&self
#2=self(only)

#~~~~~~~~~~~~~~~~~~~
#Attack Types
#~~~~~~~~~~~~~~~~~~~
#0=Dex
#1=Str
#2=Int
#3=None
Mage = {"Magic Missile" : (10, 0, 0, 2, 0, 1, 2),
		}
		
Warrior = {"Cleave" : (0, 0, 0, 1, 1, 1, 1),
		}

Ranger = {"Volley" : (0, 0, 0, 3, 1, 1, 0),
		}

Assassin = {"Poison" : (0, 0, 0, 1, 1, 1, 1),
		}
		
Paladin = {"Defend" : (0, 0, 10, 1, 1, 1, 3),
		}
		
Priest = {"Minor Heal" : (0, 10, 0, 1, 1, 1, 3),
		}
#Necromancer = {"Minor Heal" : (0, 0, 10, 1, 1),
#	}
		

#"Template" : ["strength", "intelligence", "dexterity", "vitality"],
Races = {
	"Orc" : [15, 6, 12, 12 ],
	"Dwarf" : [12, 9, 9, 15],
	"Elf" : [7, 15, 15, 8],
	}

#NOTE LIMITS TO WHAT CAN BE EQUIPPED

#"Template" : ["weapon", "armor", "boots", "helmet"],
Classes = {
	"Mage" : ("Wooden Staff", "Worn Robe", "Ragged Boots", "Linen Hood", Mage),
	"Warrior" : ("Rusty Sword", "Old Chainmail", "Worn Boots", "Rusty Helmet", Warrior),
	"Ranger" : ("Rusty Bow", "Leather Tunic", "Leather Boots", "Leather Helmet", Ranger),
	"Assassin" : (),
	"Paladin" : (),
	"Priest" : ()
	#"Necromancer" : (),
	}

def AbilityPrint(Class):
	os.system('clear')
	for ability in Class:
		#Target
		if Class[ability][4] == 0:
			if Class[ability][3] == 1:
				target = "enemy."
			else:
				target = "enemies."
		elif Class[ability][4] == 1:
			target = "allies (including self)."
		else:
			target = "self only."
		
		print "| %s: \n|" % ability
		if Class[ability][0] >= 1:
			print "| Deals %i Damage. " % Class[ability][0]
		if Class[ability][1] >= 1:
			print "| Heals for %i points of health." % Class[ability][1]
		if Class[ability][2] >= 1:
			print "| Increases Defense by %i points." % Class[ability][2]
		if Class[ability][3] >= 1:
			print "| Targets up to %i %s" % (Class[ability][3], target)
		else:
			print "| Targets %s" % target
		print "="*25
		
## STAT ORDER
# [Strength, Intelligence, Dexterity, Speed]
Weapons_Stat_List = {"Wooden Staff" : [5, 10, 0, 2],
					"Rusty Sword" : [10, 0, 5, 2],
					}
## STAT ORDER
# [Vitality, Mana, Stamina Strength, Intelligence, Dexterity, Speed]
Armor_Stat_List = {"Worn Robe" : [3, 6, 2, 2, 4, 1, 3]
					}
## STAT ORDER
# [Vitality, Mana, Stamina, Speed]		
Boot_Stat_List = {"Ragged Boots" : [1, 3, 1, 2]
					}
## STAT ORDER
# [Vitaliy, Mana, Stamina, Strength, Intelligence, Dexterity, Speed]
Helm_Stat_List = {"Linen Hood" : [2, 5, 1, 1, 4, 1, 2]
					}

BowsP = {"Wooden Bow" : [100, 1],
	"Steel Bow" : [700, 2],
	"Lightning Bow" : [1500, 3],
	"Bow of Hellfire" : [3000, 4],
	"Phantom Bow" : [6000, 5],
	"Dragon Bow" : [11000, 6],
	"Damk sword" : [20, 7],
	"rainbow sword" : [90, 8]
	}

"""
ArmorP = {"Rusty armor" : [10 , 1],
        "Steel armor" : [100 , 5],
        "Gold armor" : [1000, 40],
        "Copper armor" : [250, 20]
        }

Weapons = [BowsP]

print "Bows:\t\t\t\tPrice:"


for item in BowsP:
	print "%d.) %s   \t\t$%i \t Range Damage: +%d" % (BowsP.keys().index(item)+1, item, BowsP[item][0], BowsP[item][1])
	

print "\nArmor:\t\t\t\tPrice:"
for item in ArmorP:
	print "%d.) %s   \t\t$%i \t Damage: %d" % (ArmorP.keys().index(item)+1, item, ArmorP[item][0], ArmorP[item][1])
	"""