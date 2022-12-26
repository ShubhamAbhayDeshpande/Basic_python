albums = [("Welcome to my nightmare", "Alice Cooper", 1975),
("Bad Company", "Bad Company", 1974),
 ("Nightflight", "Budgie", 1984),
 ("More mayham", "Emilda may", 1981),
("Ride the lightening", "Metallica", 1984)]

item_1 = albums[0]
item_2 = albums[1]
item_3 = albums[2]
item_4 = albums[3]
item_5 = albums[4]


name= [item_1[0], item_2[0],item_3[0],item_4[0],item_5[0]]
album = [item_1[1], item_2[1],item_3[1],item_4[1],item_5[1]]
year = [item_1[2], item_2[2],item_3[2],item_4[2],item_5[2]]

for i in range(5):
    print("my discography:")
    print("band: {}, album: {}, year: {}".format(name[i],album[i],year[i]))

# The code below also gives the same output. But it saves us th effort of unpacking the individual tuples. 
# It is a more efficient way of writing the same code. 
for a, n, y in albums:
    print("band: {}, album: {}, year: {}".format(n,a,y))
