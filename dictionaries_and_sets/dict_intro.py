# Dictionaries are a set of key and value pair. 
vehicles = {
    'dream':'Honda 250T',
    'roadster':'BMW R1100',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier can-am 250',
    'virago':'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta':'Foard Fiesta Ghia 1.4'
}


# To retrive a value we will use the key and value pair.

my_car = vehicles['roadster']  # Important thing to note here is that, we provide the key and the dictionary name 
                            # in order to print the value of the dictionary. Care should be taken that, the written 
                            # and the actual keyname should match perfectly. Otherweise, we get an error.  
print(my_car)  # printing the value in the dictionary. 

# We can do the same thing, by using .get() method. 

print(vehicles.get('tenere'))

# Iterating over dictionaries. 
for key in vehicles:
    print(key,vehicles[key], sep = ", ")

print()
print()


# There is also a way in which we can immulate the enumerate function in the dictionaries. It can be done with teh .items() methods. We can print both the keys and the
# Values at the same time with this method. It is just the fater way of doing the same thing. But in case of larger datasets the below method is more efficient. 

for key, value in vehicles.items():
    print(key, value, sep=", ")

print()
print()

## Adding an item in the dictionary.##

# We can add items directly in the dictionary by using the keyward argument.

vehicles["reco plane"] = "Lockheed Marrtin SR71 black bird"
vehicles["toy"] = "Glider"

# Notice that there is no .append() method in the dictionaries. We can add new values directly using the keywards. This will be appended at the end of the dictionary everytime.
for key, value in vehicles.items():
    print(key, value, sep=", ")

print()
print()  

## Changing the values associated to a key and then deleting the value associated with the key.
# We can simply change the values associated with the key. 
# We will change the value of the reco plane key. The old value is completely deleted and replaced. 
# But, now the question is, what happens if we use the same key two times?


vehicles['reco plane'] = "Boing B2"

for key, value in vehicles.items():
    print(key, value, sep=", ")

print()
print()


## If we use the smae key two times, in the following dictionary we will use the key 'roadster' two times and see what happens.
vehicles = {
    'dream':'Honda 250T',
    'roadster':'BMW R1100',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier can-am 250',
    'virago':'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta':'Foard Fiesta Ghia 1.4',
    'roadster': 'Triumph 600 cc bike'
}

for key, value in vehicles.items():
    print(key, value, sep=", ")

# In the output there will be only one key value pair. The last key value pair will replace any earlier key and value pair.

## How do we delete the keys from the dictionary##
# deleting an item is similar to deleting an item from a list using del

del vehicles["roadster"]
print()
print()

for key, value in vehicles.items():
    print(key, value, sep=", ")

print()
print()

## Now the question is, what happens if we try to delete the value that does not exist in the dictionary??
# the short answer is, we get an error if we use the del. But, if we use pop(), it will just use the default value that we used instead.

vehicles.pop("f1", None)

for key, value in vehicles.items():
    print(key, value, sep=", ")

print()
print()

# Now let's see how the pop() works in the dictionary in the case when the key value actually exists.

plane = vehicles.pop("dream") 
print(plane) # This will just print the value associated with the key "dream" in the dictionary. 

# Now let's check the contents of the dictionary 
for key, value in vehicles.items():
    print(key, value, sep=", ") # As we will see after printing this line that, we get all the values exvcept the value that we just poped out.
