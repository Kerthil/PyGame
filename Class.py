import random
class Character(object):
    def __init__(self, name, atk, arm, mhp):

        self.name = name
        self.atk = atk
        self.arm = arm
        self.mhp = mhp
        self.hp = mhp

    def attack(self,atk, target):
        print str(self.name) + " attacks " + target + "."

    def take_damage(self, dmg):
        self.hp = self.hp - dmg
        print self.name + ' takes ' + str(dmg) + ' Damage! Hp: ' + str(self.hp)

    def mod_hp(self,delta):
        self.hp += delta # +for healing - for damage
        if self.hp <= 0:
            pass #Game over? back to main screen??



class Player(Character):
    def __init__(self,name,atk,arm,mhp, xp=0):
        super(Player, self).__init__(name,atk,arm,mhp)
        self.xp = xp

    def set_xp(self, gainz):  #Sets new xp after battles.
        xp += gainz
        self.level_up()

    def level_up(self): #Checks if level up, if so goto level up screen
        pass


class Enemy_factory(object): #Build enemies in a super efficient way

    """
    " EXAMPLES
    " self.enemy_lookup_table['Trent']['zone'] = ['forest'] # this means the trent is found in the forest
    " self.enemy_lookup_table['Spider']['zone'] = ['forest','cave'] # this means the spider is found in the cave and forest
    " TO GENERATE AN ENEMY...
    "   new_enemy = Character(self.enemy_lookup_table['Trent']['stats'][0],self.enemy_lookup_table['Trent']['stats'][1],
    "   self.enemy_lookup_table['Trent']['stats'][2],self.enemy_lookup_table['Trent']['stats'][3])
    """

    def __init__(self):
        self.enemy_lookup_table = {  #Name, Atk , Arm, HP
            'Trent': {
                'zone': ['forest', ],
                'stats': ['Trent', 2, 1, 1, 1]},
            'Spider': {
                'zone': ['forest', 'cave', ],
                'stats': ['Spider', 1, 1, 1, 1]},
            'Piranha Plant': {
                'zone': ['forest', ],
                'stats': ['Piranha Plant', 1, 1, 1, 1]},
            'Bat': {
                'zone': ['cave', ],
                'stats': ['Bat', 1, 1, 1, 1]},
            'Skeleton': {
                'zone': ['cave', ],
                'stats': ['Skeleton', 1, 1, 1, 1]},
        }

    def generate_enemy(self, enemy, floor):
        enemy_stat_mult = 1.5 * floor
        return Character(enemy[0], enemy[1]*enemy_stat_mult, enemy[2]*enemy_stat_mult, enemy[3]*enemy_stat_mult)

    def generate_wave(self, mission_enemy_table, floor):
        enemy_wave = []
        for i in range(3):
            enemy_wave.append(self.generate_enemy(random.choice(mission_enemy_table), floor))
        return enemy_wave

    def generate_mission(self, zone, floor):
        mission_enemy_table = []

        enemy_waves = []
        for key in self.enemy_lookup_table:
            if zone in self.enemy_lookup_table[key]['zone']:
                mission_enemy_table.append(self.enemy_lookup_table[key]['stats'])
        print mission_enemy_table
        for wave in range(3):
            enemy_waves.append(self.generate_wave(mission_enemy_table, floor))
        return enemy_waves


class combat_engine(object):

    def __init_(self):
        pass

    def deal_dmg(self, target , dmg):
        target.mod_hp(dmg)

    def combat_loop(self):
        pass
        """
        " combat loop will rotate between turns of players, and the enemy
        "  Check speed / generate turn order
        "      array_of_turns
        "      for dude in array_of_turns
        "        dude.action() # example: perform an attack
        "        all enemies dead? you win! # Handle win condition (award xp, loot, return to game loop)
        "        all allies dead? you lose! # Handle loss condition (game over, respawn, et cetra)
        "
        "
        """
thius is a a changefasdf as
"""
Tips and tricks
dfdfdsasf
Create methods when you need them, never be afriad to create a method
Keep in mind you can create methods OUTSIDE of objects.  Usually these global methods are for debugging
Lastly, your imagination is the limit, you just need to think of it one problem at a time and solve it that way
"""


# This 'main' method will execute a test sequence of gameplay to test all classes and a methods in all classes
if __name__ == "__main__":

    PC_INFO = {
        "name" : "Bob",
        "attack" : 10,
        "armor" : 10,
        "max_hp" : 100,
        "current_xp" : 0
    }

    # Create player object
    p = Player(PC_INFO["name"], PC_INFO["attack"],
               PC_INFO["armor"], PC_INFO["max_hp"], PC_INFO["current_xp"])

    # Instantiate objects
    ef = Enemy_factory()
    ce = combat_engine()

    # Create monsters (Character object) for the player to fight
    a = ef.generate_mission('cave',100)
    for element in a:
        for i in element:
            print i.name , i.atk , i.arm , i.mhp

    # Test combat
    ce.combat_loop()

