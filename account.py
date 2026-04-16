'''
Program: account.py

Programmer: Kaweny Ezidio

Date: 11/21/2022

Description: This program has a class named Account that is used to initialize
two data attributes for account holders: name and balance. The class also and
accepts deposits and withdrawal which replects on the balance of the account
holder, returns the updated balance after transactions and messages when the
user inserts deposit and withdrawal amounts that are not accepted.

'''
#idle

# Create a class called Account to represent a bank account used to store 
# customers personl information. 
class Account:

# Construct a circle object using __init__ method that initializes object’s
# data attributes. It takes 3 parameteres: self, name and balance.   
    def __init__(self, name, balance):

  # Define the attributes of the class
      
        self.__name = name
        self.__balance = balance
        
# Validate balance  using if statement to ensure it remains valid(non negative)
        if(self.__balance <= 0):
            self.__balance = 0
            
# Mutator ("set") method:

# Create a method called setBalance that accepts an argument for balance.          
    def setBalance(self, balance):
        self.__balance = balance
        
# Accessor ("get") method:

# Create a method called getBalance that returns the balance        
     
    def getBalance(self):        
        return self.__balance
    
# Create a method called get_withdraw that accepts an argument for withdrawal
                            # amount
 
    def get_withdraw(self, withdrawal):

# Validate withdrawal input using if statement to ensure it remains valid and
# account have sufficient funds
      
        if(self.__balance < withdrawal):

    # check if balance is equal or less than 0 and return message.    
            if(self.__balance <= 0):
                return "We were unable to complete this transation due to Insufficient Funds.\n"
            else:
        # otherwise let user know account limit
                return "\tWithdrawal amount exceeds balance.\nPlease enter amount less than or equal to ${:.2f}\n".format(self.__balance)

    # check if withdrawal is equal or less than 0 and return message.    
        elif(withdrawal <= 0):
            return "\tWithdrawal amount invalid.\nPlease enter amount greater than $0.00\n"
        else:
    # otherwise withdraw money from account
            self.__balance = self.getBalance() - withdrawal
            return "Transaction -${:.2f}\t\tBalance: ${:.2f}\n".format(withdrawal,self.__balance)


 # Create a method called get_deposit that accepts an argument for deposit
                            # amount         
    def get_deposit(self, deposit):
        
    # check if deposit is equal or less than 0 and return message. 
        if(deposit <= 0):
            return "\tDeposit amount invalid.\nPlease enter amount greater than $0.00\n"
        else:
        # otherwise deposit money into account
            self.__balance = self.__balance + deposit 
            return "Transaction ${:.2f}\t\tBalance: ${:.2f}\n".format(deposit,self.__balance)

# Creat a method called __str__  that returns a string containing the customer's
#personal information: name and balance.
    def __str__(self):
       return "Name: {}\t\tTotal Balance: ${:.2f}\n\n".format(self.__name, self.__balance)
