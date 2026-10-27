# ===== BAGIAN 1: Hero, Tampilkan, Penyimpanan =====

# # Class Hero hanya mengurus data & aksi hero (tugas 1: pertarungan)
# class Hero:
#     def __init__(self, name, health):
#         self.name = name
#         self.health = health
#
#     def serang(self, target):
#         target.health -= 10
#
#
# # Tugas 2: tampilan
# class TampilkanHero:
#     def menampilkanHero(self, hero):
#         print(f"{hero.name} | HP {hero.health}")
#
#
# # Tugas 3: penyimpanan
# class PenyimpananHero:
#     def menyimpanHero(self, hero, nama_file):
#         with open(nama_file, "a") as f:
#             f.write(f"{hero.name},{hero.health}\n")
#
#
# # Program utama
# esme = Hero("Esmeralda", 100)
# Hero("Benedetta", 120).serang(esme)
#
# tampilkanHero = TampilkanHero()
# tampilkanHero.menampilkanHero(esme)
#
# penyimpananHero = PenyimpananHero()
# penyimpananHero.menyimpanHero(esme, "hero_data.txt")


# ===== BAGIAN 2: Polimorfisme (dari foto) =====

# class Hero:
#     def __init__(self, attack):
#         self.attack = attack
#
#     def hitung_damage(self):
#         return self.attack
#
#
# class Fighter(Hero):
#     def hitung_damage(self):
#         return self.attack + 5
#
#
# class Mage(Hero):
#     def hitung_damage(self):
#         return self.attack + 3
#
#
# class Assassin(Hero):
#     def hitung_damage(self):
#         return self.attack + 4
#
#
# print(Fighter(10).hitung_damage())
# print(Mage(10).hitung_damage())
# print(Assassin(10).hitung_damage())

# class Unit:
#     def bergerak(self):
#         print("Unit bergerak")

# class Minion(Unit):
#     pass

# class Turret(Unit):
#     def bergerak(self): # melanggar janji parent
#         raise Exception("Turret tidak bisa bergerak!")

# def maju(unit: Unit):
#     unit.bergerak()

# maju(Minion())
# maju(Turret())

# class Unit:
#     pass # hanya yang dimiliki semua unit

# class UnitBergerak(Unit):
#     def bergerak(self):
#         print("Unit bergerak")

# class Minion(UnitBergerak):
#     pass

# class Turret(Unit): # tidak berjanji bisa bergerak
#     def tembak(self):
#         print("Turret menembak")

# def maju(unit: UnitBergerak): 
#     unit.bergerak()

# maju(Minion())
# Turret().tembak()

class PapanSkorKonsol:
    def catat(self, pesan):
        print(f"[KONSOL] {pesan}")

class Arena:
    def __init__(self):
        self.papan_skor = PapanSkorKonsol() # hardcoded
    def adu(self, a, b):
        self.papan_skor.catat(f"{a} vs {b}")

Arena().adu("Balmond", "Layla")