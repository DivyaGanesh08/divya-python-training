
from abc import ABC, abstractmethod

class BankAccount(ABC):

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance   
    def get_balance(self):
        return self.__balance

    @abstractmethod
    def calculate_interest(self):
        pass

class SavingsAccount(BankAccount):

    def calculate_interest(self):
        balance = self.get_balance()
        interest = balance * 0.04   
        return interest


# Main program
name = input("Enter Name: ")
balance = float(input("Enter Balance: "))
account = SavingsAccount(name, balance)

print("Balance:", account.get_balance())
print("Interest:", account.calculate_interest())