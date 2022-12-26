""" 
This class will help as an example in the explanation of composition in python

"""
class Wing(object):
    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("This bird can fly easily")
        elif self.ratio == 1:
            print("This bird can still fly but requires a lot of work.")
        else:
            print("This is a flightless bird")


class Duck(object):
    """
    We do not need to add the init method in this class
    """
    def __init__(self):
        self._wing = Wing(1.8) # Here we are using the class that we created above to make a new attribute of the Duck class. So now, the class duck is composed of the class Wing and 
        # access to all the methods of the wings class.

    def walk(self):
        print("The duck walks")

    def swim(self):
        print("The duck can swim")

    def quack(self):
        print("The duck can also quack")

    def fly(self): # here we are defining the method in the Duck class which is call fly method in the class Wing.
        self._wing.fly()

# we will create another class called penguine which will have all the same properties as the class Duck

class Penguine(object):
    def walk(self):
        print("Penguine can also walk")

    def swim(self):
        print("Penguine can also swim even in colder waters")

    def quack(self):
        print("Penguine cannot cannot quack but it can dance")



if __name__ == '__main__':
    donald = Duck()
    donald.fly()

    print() # to maintain separation between two tests




# What does all of this mean?
"""
This essentially means that the class Duck is now composed of a different class Wings. This is different from the inheritance and polymorphism, because, it is not inheriting anything 
from the class Wings. But rather class Wings is now a part of the class Duck.
"""
