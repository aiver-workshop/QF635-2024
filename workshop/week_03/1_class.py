"""
In object-oriented programming, A class represents an entity with properties and behavior (methods).

Reference: https://realpython.com/python3-object-oriented-programming/#what-is-object-oriented-programming-in-python

"""


# Define an Account class
class Account:
    # A constructor method to initialize account with an identifier
    def __init__(self, identifier):
        pass

    # Provide output when account object is printed
    def __str__(self):
        return "Account identifier={}, balance={:.2f}".format(self.identifier, self.balance)

    # To get balance of this account
    def balance(self):
        pass

    # to deposit money to this account
    def deposit(self, amount):
        pass

    # to withdraw money from this account
    def withdraw(self, amount):
        pass


# Define a main method
if __name__ == '__main__':
    pass
    # TODO create an account, and print the object

    # TODO deposit some money to this account, and print the object

    # TODO withdraw some money from this account, and print the object

    # TODO create another account, and print the object
