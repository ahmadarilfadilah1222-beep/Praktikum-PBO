class Hero:
    def __init__(self, name, health, attack, armor, mana=50):
        self.name = name
        self.health = health
        self.attack = attack
        self.armor = armor
        self.mana = mana

    def __str__(self):
        return f"Nama Hero: {self.name}"

    def diserang(self, jumlah):
        self.health = max(0, self.health - jumlah)


class Marksman(Hero):
    pass


class Fighter(Hero):
    pass


hero1 = Marksman("Layla", 100, 30, 10)
hero2 = Fighter("balmond", 150, 40, 20)

print(hero1)
print(hero2)

hero1.diserang(25)

print(f"Health {hero1.name}: {hero1.health}")