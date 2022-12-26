"""
This class will serve as a Superclass for the classes that we will create in main.py file.

This means that all the subclasses will have the attributes and the methods that are metioned here in the below class.

"""
# Standard python Import 
import random

class Enemy:

    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self.name = name
        self.hit_points = hit_points
        self.lives = lives
        self.alive =True

    def take_damage(self, damage):
        remaining_points = self.hit_points-damage
        if remaining_points>=0:
            self.hit_points = remaining_points
            print("I took {} opints damage and have {} points left".format(damage, self.hit_points))
        else:
            self.lives -= 1
            if self.lives>0:
                print("{0.name} lost a life".format(self))
            else:
                print("{0.name} is dead".format(self))
                self.alive=False

    def __str__(self):
        return "Name: {0.name}, lives: {0.lives}, Hit Points: {0.hit_points}".format(self)


class Troll(Enemy):

    def __init__(self, name):
        #super(Troll, self).__init__(name=name, lives=1, hit_points=23)
        super().__init__(name=name, lives=1, hit_points=23) 
        # the two mehods which are shown above are identical and will produce the same results. The second one is better way of writting it.

    def grunt(self):
        print(" I the {0.name} will try to kill you in this game ".format(self))



    

    # def __init__(self, name): # What will happen now is the python will call the init method in our troll class. This means that we will not call  the init method in the superclass Enemy directily
    #     Enemy.__init__ (self, name=name, lives=1, hit_points=23)# If we still want to access the attributes from the Enemy's init method, we will have to call that here. If we just keep it like this, it will give us an error.

class Vampyre(Enemy):
    def __init__(self, name):
        super().__init__(name=name, lives=3, hit_points=12)

    def _dodges(self):
        if random.randint(1,3) == 3:
            print("*** {0.name} dodged***".format(self))
            return True
        else:
            return False

    def take_damage(self, damage):
       if not self._dodges():
        super().take_damage(damage=damage)

class VampyreKing(Vampyre):
    def __init__(self, name):
        super().__init__(name)
        self.hit_points =140


    def take_damage(self, damage):
        damage_for_king = damage/4
        super().take_damage(damage=damage_for_king)
        



        

