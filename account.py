"""
Fayaz Shaik

# bank-application-py
Repository for same Bank Application Program in Python

Bank Application with 3 types of Account:
1.⁠ ⁠Credit Account
2. ⁠Debit Account
3. ⁠Hybrid Account (linked to current but if no balance then can use credit)

The program allows:
1.⁠ ⁠Create Customer, user can have multiple accounts
2.⁠ ⁠Search by customer number or account number to display details
3.⁠ ⁠Allow credit/debit/check balance
4.⁠ ⁠Use file system to persist the data so when I rerun program should be able to retrieve the data
5.⁠ ⁠Create few Test cases

"""

import random

ACCOUNT_TYPES = ["Credit Account", "Debit Account", "Hybrid Account"]

customers = {}  # {customer_number: Customer object}
all_accounts = {}  # {account_number: Account object}
class Customer:
    def __init__(self, name, customer_number):
        self.name = name
        self.customer_number = customer_number
        self.accounts = []  # List to hold multiple accounts for the customer
        # self.balance = 0.0

    def add_account(self, account):
        self.accounts.append(account)
        all_accounts[account.account_number] = account
        print(f"Account {account.account_number} added for customer {self.name}")
    def show_all_accounts(self):
        print(f"\nCustomer: {self.name} (ID: {self.customer_number})")
        print("All Accounts:")
        for i, account in enumerate(self.accounts, 1):
            print(f"{i}. Account #{account.account_number} - {account.account_type} - Balance: ${account.balance:.2f}")

def search_customer():
    """
    Search by customer number and display all their accounts
    """
    customer_number = int(input("Enter customer number: "))
    
    if customer_number in customers:
        customer = customers[customer_number]
        print(f"\nCustomer Found!")
        print(f"Customer Name: {customer.name}")
        print(f"Customer Number: {customer.customer_number}")
        customer.show_all_accounts()
    else:
        print("No customer exists with this customer number.")
    
class Account:
    def __init__(self, name, customer_number, account_number):
        self.name = name
        self.customer_number = customer_number
        self.account_number = account_number
        self.account_type = "Base Account"
        self.balance = 0.0

def show_balance():
    
    account_number = int(input("Enter account number: "))
    if account_number in all_accounts:
        account = all_accounts[account_number]
        print(f"Customer: {account.name}")
        print(f"Account Number: {account.account_number}")
        print(f"Account Type: {account.account_type}")
        print(f"Your balance is ${account.balance:.2f}")
    else:
        print("Account not found.")

def deposit(customer):
    
    account_number = int(input("Enter account number: "))
    if account_number in all_accounts:
        account = all_accounts[account_number]
        
        amount = float(input("Enter an amount to be deposited: "))
    
        if amount < 0:
            print("That's not a valid amount")
            return 0
        else:
            customer.balance += amount
            return amount
    else:
        print("Account not found.")
        return 0

def withdraw(account):
    
    account_number = int(input("Enter account number: "))
    if account_number in all_accounts:
        account = all_accounts[account_number]
        amount = float(input("Enter an amount to be withdrawn: "))
    
        if amount < 0:
            print("Amount must be greater than 0")
            return 0
        return amount
    else:
        print("Account not found.")
        return 0
class CreditAccount(Account):
    def __init__(self, name, customer_number, account_number):
        super().__init__(name, customer_number, account_number)
        self.account_type = "Credit Account"
        # self.credit_limit = 5000

    def withdraw(customer):
        amount = float(input("Enter amount to withdraw: "))
        # '''
        # based on account type it will allow withdrawal
        # '''
        # if customer.account_type == "Credit Account":
        #     ''' 
        #     for credit it has limit of -5000
        #     '''
        if amount < 0:
                print("Amount must be greater than 0")
                return 0
        elif (customer.balance - amount) < -5000:
                print("Credit limit exceeded. Maximum credit limit is $5000")
                return 0
        else:
                self.balance -= amount
                print(f"Withdrawal successful. New balance is ${self.balance:.2f}")
                return amount
            
            
class DebitAccount(Account):
    def __init__(self, name, customer_number, account_number):
        super().__init__(name, customer_number, account_number)
        self.account_type = "Debit Account"

    def withdraw(customer):
        amount = float(input("Enter amount to withdraw: "))

        '''
        for debit it cannot go negative
        '''
        if amount > customer.balance:
            print("Insufficient Funds")
            return 0
        elif amount < 0:
            print("Amount must be greater than 0")
            return 0
        else:
            self.balance -= amount
            print(f"Withdrawal successful. New balance is ${self.balance:.2f}")
            return amount
        
# Class HybridAccount(Account):
#     def __init__(self, name, customer_number, account_number):
#         super().__init__(name, customer_number, account_number)
#         self.account_type = "Hybrid Account"

    # def withdraw(customer):
    #     amount = float(input("Enter amount to withdraw: "))
    #     if amount < 0:
    #         print("Amount must be greater than 0")
    #         return 0
    #     elif (customer.balance - amount) < -5000:
    #         print("Credit limit exceeded. Maximum credit limit is $5000")
    #         return 0
    #     else:
    #         self.balance -= amount
    #         print(f"Withdrawal successful. New balance is ${self.balance:.2f}")
    #         return amount


def create_account():
    print("Create New Account")
    
    choice = input("Do you want to create a new customer? (y/n): ")
    if choice.lower() == 'n':
        customer_number = int(input("Enter existing customer number: "))
        if customer_number not in customers:
            print("Customer not found. Please create a new customer first.")
            return None
        customer_obj = customers[customer_number]
        name = customer_obj.name  # Use existing customer's name
    else:
        name = input("Enter customer name: ")
        customer_number = random.randint(10000, 99999)
        while customer_number in customers:  # Ensure unique customer number
            customer_number = random.randint(10000, 99999)
        customer_obj = Customer(name, customer_number)
        customers[customer_number] = customer_obj
        
        
    # name = input("Enter customer name: ")
    
    print("Select Account Type:")
    print("1. Credit Account (Can go negative up to $5000)")
    print("2. Debit Account (Cannot go negative)")
    # print("3. Hybrid Account)
    
    while True:
        account_choice = input("Enter your choice (1-3): ")
        if account_choice == '1':
            account_type = ACCOUNT_TYPES[0]  # "Credit Account"
            break
        elif account_choice == '2':
            account_type = ACCOUNT_TYPES[1]  # "Debit Account"
            break
        # elif account_choice == '3':
        #     account_type = "Hybrid Account"
        #     break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
    
    
    account_number = random.randint(1000000000, 9999999999)
    while account_number in all_accounts:
        account_number = random.randint(1000000000, 9999999999)
    '''
    Create Customer Account
    '''
    if account_type == ACCOUNT_TYPES[0]:
        account_obj = CreditAccount(name, customer_number, account_number)
    elif account_type == ACCOUNT_TYPES[1]:
        account_obj = DebitAccount(name, customer_number, account_number)
    # elif account_type == "Hybrid Account":
    #     account_obj = HybridAccount(name, customer_number, account_number)

    customer_obj.add_account(account_obj)
    all_accounts[account_number] = account_obj

    print(f"\nAccount created successfully!")
    print(f"Customer Name: {account_obj.name}")
    print(f"Customer Number: {account_obj.customer_number}")
    print(f"Account Number: {account_obj.account_number}")
    print(f"Account Type: {account_obj.account_type}")
    print(f"Initial Balance: ${account_obj.balance:.2f}")

    return account_obj

def show_customer_accounts():
    customer_number = int(input("Enter customer number: "))
    if customer_number in customers:
        customers[customer_number].show_all_accounts()
    else:
        print("Customer not found.")