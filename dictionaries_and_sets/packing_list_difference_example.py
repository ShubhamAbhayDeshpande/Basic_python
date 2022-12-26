"""
In this program we will see how to use discard() to remove items from the set and why using discard() here is a better option than using remove()

"""
travel_mode = {"1": "car", "2": "plane"}

items = {
    "can opener",
    "fuel",
    "jumper",
    "knife",
    "matches",
    "razor blades",
    "razor",
    "scissors",
    "shampoo",
    "shaving cream",
    "shirts (3)",
    "shorts",
    "sleeping bag(s)",
    "soap",
    "socks (3 pairs)",
    "stove",
    "tent",
    "mug",
    "toothbrush",
    "toothpaste",
    "towel",
    "underwear (3 pairs)",
    "water carrier",
}

restricted_items = {
    "catapult",
    "fuel",
    "gun",
    "knife",
    "razor blades",
    "scissors",
    "shampoo",
}

print("Please choose your mode of travel:")
for key, value in travel_mode.items():
    print(f"{key}: {value}")
    # Python 3.5 and earlier
    # print("{}: {}".format(key, value))

mode = "-"
while mode not in travel_mode:
    mode = input("> ")

if mode == "2":
    # We want to modify the original packing list. We can do that with difference_update() method.

    items.difference_update(restricted_items) # same thing can be done by the differece() method. But, that will create a new set.
    # for restricted_item in restricted_items:
    #     items.discard(restricted_item)# Here discard() is the right choice because we do not care if the restricted_item is in the items set or not.
    # #pass #This is a dummy pass 

# print the packing list
print("You need to pack:")
for item in sorted(items):
    print(item)
