from player import Player

shubham = Player("Tim")

print(shubham.name)
print(shubham.lives)
shubham.lives -= 1
print(shubham)

shubham.lives -= 1
print(shubham)

shubham.lives -= 1
print(shubham)

shubham.lives -= 1
print(shubham)

shubham._lives = 9
print(shubham)

shubham.level = 2
print(shubham)

shubham.level += 5
print(shubham)

shubham.level = 3
print(shubham)

shubham.score = 230
print(shubham)


