from player import Player

# create a player
shubham = Player("Shubham")

# create a random monster as an enemy
from enemy import Enemy, Troll, Vampyre, VampyreKing
random_monster = Enemy("random_monster", 20, 1)
random_monster.take_damage(12)
print(random_monster)


ugly_troll = Troll("Ogg")
print("Ugly troll -{}".format(ugly_troll))

another_troll = Troll("Ug")
print("Another troll -{}".format(another_troll))

brother_to_another = Troll("Urg")
print("brother_to_anoter -{}".format(brother_to_another))

ugly_troll.grunt()
another_troll.grunt()
brother_to_another.grunt()

ugly_troll.take_damage(6)
another_troll.take_damage(9)
brother_to_another.take_damage(10)

print() # for separation in the output

vamp1 = Vampyre("drac")
print(vamp1)
vamp1.take_damage(7)

vamp2 = Vampyre("drac_minion")
print(vamp1)
vamp1.take_damage(6)

# vamp1 will take damage until his lives are over.
while vamp1.alive:
    vamp1.take_damage(1)
    #print(vamp1)

vlad = VampyreKing("vlad")

while vlad.lives:
    vlad.take_damage(12)
