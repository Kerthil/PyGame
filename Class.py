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

class Enemy(Character):

class Boss(Character):



def damage(atk,arm): #Calculates damage
    return atk - arm   #Attacker's attack - defender's defense Returns damage





Kerthil = Player("Kerthil", 5, 2, 10)

print Kerthil.atk
print Kerthil.arm
print Kerthil.mhp
print Kerthil.hp

Kerthil.take_damage(2)

print Kerthil.hp

Zgrill = Player("Zgrill",2,3,12)


