'''
Class with Private Attributes and Getter/Setter
Create a class BankAccount with a private attribute balance.
Write methods deposit to increase the balance and withdraw to decrease the balance,
       ensuring the balance never goes negative. Add get_balance to return the balance.
'''

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Account Balance Updated")
        else:
            print("Amount should be greater than 0")

    def withdrawl(self, amount):

        if (amount >= self.__balance) or (self.__balance - amount <= 0):
            print("Insufficient Funds in Account")
        else:
            self.__balance -= amount
            print("Funds Withdrawn")

account = BankAccount(7000)
print(account.get_balance())
#print(account.__balance)
account.deposit(20000)
print(account.get_balance())
account.withdrawl(40000)
account.withdrawl(5000)
print(account.get_balance())