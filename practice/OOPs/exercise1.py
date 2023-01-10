"""
Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.

"""
# class with instance variable (parameterized instance variable)
class Vehicle:

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


# class without any instance variable and method.
class Vehicle:
    pass


# class with a method to calculate the rpm from the maximum speed
class Vehicle:

    def __init__(self, max_speed, mileage, radius, Logo = None):

        self.max_speed = max_speed
        self.mileage = mileage
        self.radius = radius
        self.Logo = Logo

    def rpm(self):
        RPM = (self.max_speed * 60) / (self.radius * 2 * 3.147)
        return RPM 


class Bus(Vehicle):
    def __init__(self, max_speed, mileage, radius, passanger_capacity):
        super().__init__(max_speed, mileage, radius)
        self.passanger_capacity = passanger_capacity

    def capcity(self):
        print("The passanger capcity of the bus is", self.passanger_capacity)

    def display(self):
        print("max speed: {}, Milage: {}, Radius: {}".format(self.max_speed, self.mileage, self.radius))


tata = Bus(120, 10, 24, 30)
wheel_speed = tata.rpm
print(tata.Logo)

print("Bus rpm ", wheel_speed)
tata.capcity
tata.display



    
    




