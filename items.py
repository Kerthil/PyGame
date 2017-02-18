class Item(object):
    def __init__(self, name, des):
        self.name = name
        self.des = description



"""
"To Do:
"1. check if object generated already, add on hand.
"""
def gen_item(id):
    if id == 1: #Potion
        I1 = Item("Potion", "A simple potion used to heal 5 hp.")
    if id == 2: #Super Potion
        I1 = Item("Super Potion", "An advanced potion used to heal 10 hp.")