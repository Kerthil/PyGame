class Item(object):
    def __init__(self, name, des, qoh=0):
        self.name = name #Item name
        self.des = description #Item Description
        self.qoh = q #Quanity of item


def add_item(id):
    if id == 1: #Potion
        I1 = Item("Potion", "A simple potion used to heal 5 hp.")
    if id == 2: #Super Potion
        I1 = Item("Super Potion", "An advanced potion used to heal 10 hp.")

