"""
In object-oriented programming, A class represents an entity with properties and behavior (methods).

Reference: https://realpython.com/python3-object-oriented-programming/#what-is-object-oriented-programming-in-python

"""


# Define an Account class
class Account:
    # A constructor method to initialize account with an identifier
    def __init__(self, identifier):
        self.identifier = identifier
        self.balance = 0

    # Provide output when account object is printed
    def __str__(self):
        return "Account identifier={}, balance={:.2f}".format(self.identifier, self.balance)

    # To get balance of this account
    def balance(self):
        return self.amount

    # to deposit money to this account
    def deposit(self, amount):
        self.balance += amount

    # to withdraw money from this account
    def withdraw(self, amount):
        self.balance -= amount


# Define a main method
if __name__ == '__main__':
    # create an account, and print the object
    account_1 = Account('ABC')
    print(account_1)

    # deposit some money to this account, and print the object
    account_1.deposit(100.50)
    print(account_1)

    # withdraw some money from this account, and print the object
    account_1.withdraw(20.15)
    print(account_1)

    # create another account, and print the object
    account_2 = Account('XYZ')
    print(account_2)

