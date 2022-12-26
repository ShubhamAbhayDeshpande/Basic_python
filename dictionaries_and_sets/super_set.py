animals= {'turtle', 'horse', 'robin', 'python', 'swallow', 'hedgehog', 'wern', 'Aardvark', 'Cat'}
bird= {'robin', 'swallow', 'wren'}

# To check if the birds is a subset of the animals set. By using .issubset() and .issuperset()

print(f"bird is a subset of animals: {bird.issubset(animals)}")
print(f"animals is a superset of birds: {animals.issuperset(bird)}")


