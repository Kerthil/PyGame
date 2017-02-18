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
        self.enemy_lookup_table = {
            'Trent': {
                'zone': ['forest', ],
                'stats': ['Trent', 1, 1, 1, 1]},
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

    def generate_enemy(self, enemy):
        return Character(enemy[0], enemy[1], enemy[2], enemy[3])

    def generate_wave(self, mission_enemy_table, floor):
        enemy_wave = []
        for i in range(3):
            enemy_stat_mult = 1.5 * floor
            for stat in mission_enemy_table[i][1:]:
                stat *= enemy_stat_mult
            enemy_wave.append(self.generate_enemy(random.choice(mission_enemy_table)))
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


class Boss(Character):
    pass


def damage(atk,arm): #Calculates damage
    return atk - arm   #Attacker's attack - defender's defense Returns damage




if __name__ == "__main__":
    Kerthil = Player("Kerthil", 5, 2, 10)

    print Kerthil.atk
    print Kerthil.arm
    print Kerthil.mhp
    print Kerthil.hp

    Kerthil.take_damage(2)

    print Kerthil.hp

    Zgrill = Player("Zgrill",2,3,12)


