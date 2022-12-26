"""We have some data that contains a mixture of flowers and shrubs, in a list.



Our customer would like two separate lists.

One, called flowers, will contain only flowers, and the other, not surprisingly called shrubs, must contain only shrubs."""

data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac - Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

flowers = []
shrubs = []

for item in data: 
    if "Flower" in item:
        flo = item.split("-")[0]
        flowers.append(flo)

    else:
        shu = item.split("-")[0]
        shrubs.append(shu)

print("The data contains these flowers: ")
print(flowers)

print(" ")

print("The data contains these scrubs")
print(shrubs)

