MAX_HEALTH = 100
class Player:
    def __init__(self, name):
        self.name = name
        self.health = MAX_HEALTH
        self.gold = 0
        self.inventory = []

    def show_stats(self):
        if self.inventory:
            items = ", ".join(self.inventory)
        else:
            items = "empty"
        print()
        print(f"❤️  Health: {self.health}   💰 Gold: {self.gold}   🎒 Inventory: {items}")
        print("-" * 50)

    def take_damage(self, amount):
        self.health = max(self.health - amount, 0)

    def heal(self, amount):
        self.health = min(self.health + amount, MAX_HEALTH)

    def is_alive(self):
        return self.health > 0

    def add_gold(self, amount):
        self.gold += amount

    def add_item(self, item):
        self.inventory.append(item)

    def potion_count(self):
        return self.inventory.count("potion")

    def drink_potion(self):
        if self.potion_count() > 0:
            self.inventory.remove("potion")
            self.heal(30)
            return True
        else:
            return False
