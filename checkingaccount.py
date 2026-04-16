'''
Program: checkingaccount.py

Programmer: Kaweny Ezidio

Date: 11/21/2022

Description: This program has a class named CheckingAccount which is a subclasse
that inherits data from the Account class, includes a data attribute
indicating a transaction fee and redifine methods deposit and withdraw so that
they subtract the fee from the account balance whenever either transaction is
performed.

'''
#idle

#import Account Class from account file to create subclass and use data
from account import Account

# Create a class called CheckingAccount that inherits data from the Account class      
class CheckingAccount(Account):

# Construct a circle object using __init__ method that calls the initializer
# method of the superclass(Account) and then initializes the unique data
# attributes: fee
    def __init__(self, name, balance, fee):
        Account.__init__(self,name, balance)
        self.__fee = fee
    
# Redifine method called get_withdraw that accepts an argument for withdrawal
                # amount and adds fee to transaction
    def get_withdraw(self, withdrawal):
        self.__withdrawal = withdrawal + self.__fee # add fee to transaction
        account_limit =  self.getBalance() - self.__fee # define account limit
        
# Validate withdrawal input using if statement to ensure it remains valid and
# account have sufficient funds
        if(self.getBalance() < self.__withdrawal):
            if(self.getBalance() <= (self.__fee)): 
                return "We were unable to complete this transation due to Insufficient Funds.\n"
            else:
                return "\tWithdrawal amount exceeds balance.\nPlease enter amount less than or equal to ${:.2f}\n".format(account_limit)

    # otherwise withdraw money from account and update balance 
        else:
            # subtract fee from balance
            balance =  self.getBalance() - self.__withdrawal 
            self.__balance = balance # update balance
            Account.setBalance(self,balance) # update balance for superclass
             # return transaction
            return "Transaction -${:.2f}\t\tBalance: ${:.2f}\n".format(self.__withdrawal,self.__balance)

# Redifine method called get_deposit that accepts an argument for deposit
                # amount and adds fee to transaction         
    def get_deposit(self, deposit):
        self.__deposit = deposit - self.__fee # subtract fee from deposit
        balance = self.getBalance() + self.__deposit # update balance
        self.__balance = balance
        Account.setBalance(self,balance) # update balance for superclass
       # return transaction
        return "Transaction ${:.2f}\t\tBalance: ${:.2f}\n".format(self.__deposit,self.__balance)
 
