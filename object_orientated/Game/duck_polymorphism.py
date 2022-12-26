""" 
This class will help as an example in the explanation of polymorphism in python

"""

class Duck(object):
    """
    We do not need to add the init method in this class
    """
    def walk(self):
        print("The duck walks")

    def swim(self):
        print("The duck can swim")

    def quack(self):
        print("The duck can also quack")

# we will create another class called penguine which will have all the same properties as the class Duck

class Penguine(object):
    def walk(self):
        print("Penguine can also walk")

    def swim(self):
        print("Penguine can also swim even in colder waters")

    def quack(self):
        print("Penguine cannot cannot quack but it can dance")




# create a function to check the class duck
def test_duck(duck):
    duck.walk()
    duck.swim()
    duck.quack()

if __name__ == '__main__':
    donald = Duck()
    test_duck(donald)

    print() # to maintain separation between two tests

    # we can use our test_duck function to test the class Penguine
    Pico = Penguine()
    test_duck(Pico)


# What does all of this mean?
"""
This is a major difference between a dynamically typed language like Python and a statically typed language like Java and C++- In statically typed language, 
you need to define/ declare a type of a variable when you create it. That is not the case with python. This is consequently also a good example of polymorphism in python.

"""
