'''
Ecapsulation: Protecting a class from external modifcation. 
This is enforced through access modifiers: 
- Keywords used to set visibikity or accessibility of our classes, methods, properties:
 Public, Private, Protected
'''

#Marines bank
class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance


    # this can also be a setter method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return amount
        return "insufficient balance"

    # #getter method
    # def get_balance(self):
    #     # The logic to identify the owner comes here
    #     return self.__balance
    

    # #Setter method
    # def set_balance(self, amount):
    #     if amount > 0:
    #         self.__balance = amount


    #Making our code more Pythonic
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, amount):
        if amount > 0:
            self.__balance = amount
        else:
            raise ValueError("The amount can not be less than zero")



newAccount = BankAccount('Chloe', 500000)
newAccount.deposit(300000)

print(newAccount.balance)
newAccount.balance = 200

print(newAccount.balance)




# print(f"You have successfully withdrawn {newAccount.withdraw(100000)}")

# print(f"Your new balance is {newAccount.get_balance()}")


# # Admin right is required

# newAccount.__balance = 30000

# print(f"The owner new balance is {newAccount.get_balance()}")




