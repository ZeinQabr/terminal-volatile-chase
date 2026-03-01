from data import survivor_needs
from volatilechase import clearscreen, clearinput
import random as rd

class Stuffs:
    def __init__(self):
        self.weapon = None
        self.consumable = None
        self.craftingpart = None
        self.rareitem = None

    def add_item(self, category, item):
        if category == "weapons":
            self.weapon = item
        elif category == "consumables":
            self.consumable = item
        elif category == "crafting_parts":
            self.craftingpart = item
        elif category == "rareitems":
            self.rareitem = item

    def what_players_got(self):
        return self.weapon, self.consumable, self.craftingpart, self.rareitem


def loots(player):
    category = rd.choice(list(survivor_needs.keys()))
    count = rd.randint(4, 5)
    items = rd.sample(survivor_needs[category], count)

    print(f"You found some {category}:")
    for i, item in enumerate(items, 1):
        print(f"{i}. {item}")

    choice = int(input("Choose one item (number): "))
    chosen_item = items[choice - 1]

    player.add_item(category, chosen_item)
    print(f"You took: {chosen_item}")


player = Stuffs()

for _ in range(3):
    loots(player)

print("Final inventory:", player.what_players_got())

