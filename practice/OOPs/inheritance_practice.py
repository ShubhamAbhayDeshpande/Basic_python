class Employe:
    """
    This is the base class that will be used to make sub classes later on.
    
    """
    # Defining a class variable for future use
    increment = 1.04

    def __init__(self, name, last_name, salary):
        self.name = name
        self.last_name = last_name
        self.salary = salary

    def full_name(self):
        return '{0} {0} '.format(self.name, self.last_name)

    def apply_raise(self):
        self.salary = self.salary * self.increment
        print(self.salary)
        return self.salary

# make a fucntion that will inherit from the employe class
class Developer(Employe):
    # We can make changes to the sub class and this will not affect the parent class of Employe
    increment = 1.08

    # if we want to pass an additional argument like programming method that is not a part of Employe class, we can use the constructor as shown in the below.
    def __init__(self, name, last_name, salary, prog_lang = None):
        super().__init__(name, last_name, salary)
        self.prog_lang = prog_lang

    def show_lang(self):
        print('This developer uses ', self.prog_lang)


# Now making a class called manager and this will have a attribute where you can provide the list of people which he will supervise
class Manager(Employe):

    def __init__(self, name, last_name, salary, boss_of = []): # It is not recommended to pass an mutable argument as a default argument. But in this case it is fine for the example.
        super().__init__(name, last_name, salary)
        self.boss_of = boss_of

    def show_subs(self):
        print('{} is the manager and working under him/her are {}, {}'.format(self.name, self.boss_of[0], self.boss_of[1]))

 

if __name__ == '__main__':
    emp_1 = Developer('Shubham', 'Deshpande', 70000, 'python')
    emp_2 = Developer('Shrinu', 'Chappidi', 70000)

    # What is the developer pay and what is it after the increment. This will mean that the Developer class will inherit all the methods from the employe class.
    print(emp_1.salary)
    emp_1.apply_raise()
    emp_1.show_lang()

    man_1 = Manager('Shan', 'Rehman', 100000, ['Shubham', 'Shrinu'])
    man_1.show_subs()

    # If you want to know how the classes are inheriting from the other classes, use the help() function
    #print(help(Developer))

