welcome = "Welcome to my nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1984
imedia = "More mayham", "Emilda may", 1981
metallica = ["Ride the lightening", "Metallica", 1984]

#Changing the variables to the list so that we can change the album name. 

metallica2 = list(metallica)

metallica[0] = "master of puppets"
metallica[2] = 1985

print(metallica2)

print(metallica)
print(metallica[0])
print(metallica[1])
print(metallica[2])

print(welcome) # Notice how the difference is there in the list and tuple. 




