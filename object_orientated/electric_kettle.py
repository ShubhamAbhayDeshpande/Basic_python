class kettle(object):
    # Defining the energy source for the electric kettle as a class attribute as it will not change with the instance
    # this will be the class attribute
    power_source = 'electricity'

    # The following are the instance/data attributes
    def __init__(self, make, price):
        """
        __init__ is called a constructor in python. This constructor will define all the variables that will be used by the instance of the class and the methods 
        the constructor is called every time an instance of a class is created. 
        associated with the class. Since these variables are common to all instnaces, the first argument to the constructor is 'self'. 
        the 'self' here refrences an instnace of the class.
        The variables which are associated with the instance of the class are called attributes.
        
        """
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
            self.on = True

# Let's create some instances for the class above. This is called 'instanciation'
kennwood = kettle("keenwood", 8.99)
print('make ', kennwood.make)
print('price in euros ', kennwood.price)
kennwood.power_source = 'gas'
print('power source ', kennwood.power_source)

# We can change the property of the object after it was assigned
kennwood.price = 12.9

# Another instance of the same class looks like this:
hamilton = kettle("hamilton", 10)
print('make ', hamilton.make)
print('price in euros ', hamilton.price)
print('power source ', hamilton.power_source)

# we can specify the attributes of the objects in the string 
print("Models: {0.make} = {0.price} and {1.make} = {1.price}".format(kennwood, hamilton))

# Let's use the method and change the object attribute for the hamilton object
print(hamilton.on) # should print False
hamilton.switch_on() # we do not need to pass the instance as a first parameter as because python does this automatically.
print(hamilton.on) # should print True

# Othe way of calling the class method with the class name
kettle.switch_on(kennwood) # This time we need to pass the instance for the method
print("for kennwood after state change in kennwood.on: ", kennwood.on)

# we can create a attribute for an object anywhere in python. But you need to assign a value to the new instance.
# Generally sub-classes are prefered than adding an extra attribute. 
hamilton.power = 15
print("attribute created outside for the hamilton object 'hamilton.power': ", hamilton.power)