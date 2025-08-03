'''

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


'''

import random

class Customer_account:
    def __init__(self, name, customer_number, account_number, account_type):
        self.name = name
        self.customer_number = customer_number
        self.account_number = account_number
        self.account_type = account_type
        self.balance = 0.0

# def search_account(customer):
#     if customer.customer_number in Customer_account:
#         customer_account = Customer_account[customer.customer_number]
#         print(f"Customer: {customer_account.name}")
#         print(f"Account Number: {customer_account.account_number}")
#         print(f"Account Type: {customer_account.account_type}")
#     else:
#         print("No account found.")

def show_balance(customer):
    print(f"Customer: {customer.name}")
    print(f"Account Number: {customer.account_number}")
    print(f"Account Type: {customer.account_type}")
    print(f"Your balance is ${customer.balance:.2f}")

def deposit(customer):
    amount = float(input("Enter an amount to be deposited: "))
    
    if amount < 0:
        print("That's not a valid amount")
        return 0
    else:
        return amount

def withdraw(customer):
    amount = float(input("Enter amount to withdraw: "))
    '''
    based on account type it will allow withdrawal
    '''
    if customer.account_type == "Credit Account":
        ''' 
        for credit it has limit of -5000
        '''
        if amount < 0:
            print("Amount must be greater than 0")
            return 0
        elif (customer.balance - amount) < -5000:
            print("Credit limit exceeded. Maximum credit limit is $5000")
            return 0
        else:
            return amount
    
    elif customer.account_type == "Debit Account":
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
            return amount
    
    # elif customer.account_type == "Hybrid Account":
    #     if amount < 0:
    #         print("Amount must be greater than 0")
    #         return 0
    #     else:
    #         return amount

def create_account():
    print("Create New Account")
    name = input("Enter customer name: ")
    
    print("Select Account Type:")
    print("1. Credit Account (Can go negative up to $5000)")
    print("2. Debit Account (Cannot go negative)")
    # print("3. Hybrid Account)
    
    while True:
        account_choice = input("Enter your choice (1-3): ")
        if account_choice == '1':
            account_type = "Credit Account"
            break
        elif account_choice == '2':
            account_type = "Debit Account"
            break
        # elif account_choice == '3':
        #     account_type = "Hybrid Account"
        #     break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
    
    '''
    Generate Random Customer and Account Numbers
    '''
    customer_number = random.randint(10000, 99999)
    account_number = random.randint(1000000000, 9999999999)
    '''
    Create Customer Account
    '''
    customer = Customer_account(name, customer_number, account_number, account_type)
    
    print(f"\nAccount created successfully!")
    print(f"Customer Name: {customer.name}")
    print(f"Customer Number: {customer.customer_number}")
    print(f"Account Number: {customer.account_number}")
    print(f"Account Type: {customer.account_type}")
    print(f"Initial Balance: ${customer.balance:.2f}")
    
    return customer