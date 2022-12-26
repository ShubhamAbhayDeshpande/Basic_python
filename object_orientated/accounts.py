import datetime
import pytz

class Account:
    """
    Simple class with the account information
    
    """
    # if we are going to add the time for printing the deposite and withdraw, it does not make scence to print the datetime command in the append() again and again.
    # so we can make a staticmethod here which will return the datetime and call that mehod when we want to print or add the datetime at any place.
    @staticmethod
    def _current_time():
        """This is a staticmethod which is indicated by the underscore in its _name.
        This also means that this method is by default accessible to all instances of the class. Hence we do not need to invoke 'self' as first argument for this method.
        """
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, _name, __balance):
        self._name = _name
        self.__balance = __balance
        print("account created for: ", self._name)
        if __balance > 0:
            print(f"the initial __balance in the account of {_name} is {__balance}")       
        self.trascation_list = []

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.check_balance()
            self.trascation_list.append((Account._current_time(),amount)) # This is an example where the python will unpack the tuple and assign the value to
            # date and amount in one .append() statement. 
            
        else:
            raise ValueError("Check the amount entered")
    
    def withdraw(self, amount):
        if amount > 0:
            self.__balance -= amount # Take care of the sign here. Since the amount is a negative number, we need to add it to show correct __balance.
            self.check_balance()
            self.trascation_list.append((Account._current_time(),-amount))
        else:
            raise ValueError("Check the amount entered")

    def check_balance(self):
        print("__balance in the account of {} is {} ".format(self._name, self.__balance))

    def show_transaction(self):
        for date, amount in self.trascation_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} local time was {} ".format(amount, tran_type, date, date.astimezone()) ) 


""" Create  an account for your self and deposite 10000 in it"""

if __name__ == "__main__":

    shubham = Account('shubnham', 0)
    shubham.deposit(10000)
    shubham.withdraw(1000)
    shubham.show_transaction()

    # What happens when we take an account with some initial __balance
    sanchit = Account('sanchit',800)
    sanchit.deposit(100)
    sanchit.__balance = 200
    sanchit.withdraw(200)
    sanchit.show_transaction()
    print(sanchit.__dict__)
    