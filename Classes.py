from Items import *

class Player:
	def __init__(self, name, cclass):
		self.name = name
		self.race = ""
		self.cclass = cclass
		self.skilltree = self.cclass[1][4]
		self.skills = [] 
		#Player Stats
		self.max_mana = 100
		self.base_max_health = 100
		self.max_stamina = 100
		self.stamina = self.max_stamina
		self.health = self.max_health
		self.mana = self.max_mana
		self.attack = 20
		self.base_strength = 0
		self.base_intelligence = 0
		self.base_dexterity = 0
		self.base_vitality = 0
		self.base_speed = 10
		#Player Equipment
		self.boots = " "
		self.weap = " "
		self.armor = " "
		self.helm = " "
		self.misc = " "
		self.inventory = []
		self.arrows = 0
		
	
	@property 
	def max_health(self):
		max_health = self.base_max_health 
		#max_health += int((self.base_vitality*10)/1.5)
		return max_health
		
	@property
	def max_stamina(self):
		max_stamina = self.base_max_stamina
		return max_stamina
	
	@property
	def strength(self):
		strength = self.base_strength
		for weapon in Weapons_Stat_List:
			if self.weap == weapon:
				strength += Weapons_Stat_List[weapon][0]
		return strength
	
	@property
	def speed(self):
		speed = self.base_speed
		for weapon in Weapons_Stat_List:
			if self.weap == weapon:
				speed += Weapons_Stat_List[weapon][3]
		for armor in Armor_Stat_List:
			if self.armor == armor:
				speed += Armor_Stat_List[armor][6]
		for helm in Helm_Stat_List:
			if self.helm == helm:
				speed += Helm_Stat_List[helm][6]
		for boot in Boot_Stat_List:
			if self.boots == boot:
				speed += Boot_Stat_List[boot][0]
		#speed += BowsP[self.Bow][1]
		return speed
	
class Monster: 
	def __init__(self, name, power, health):
		self.name = name
		self.power = 10
		self.health = 10
		
