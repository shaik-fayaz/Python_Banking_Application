import account

def main():
    customer_obj = None
    is_running = True

    while is_running:
        print("Banking Application")
        print("1. Create Account")
        print("2. Show Balance")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            customer_obj = account.create_account()
        # elif choice == '2':
        #     # search account details by account info
     # customer_account.search_account(customer_obj)
        elif choice == '2':
            if customer_obj:
                account.show_balance(customer_obj)
            else:
                print("Please create an account first!")
        elif choice == '3':
            if customer_obj:
                amount = account.deposit(customer_obj)
                # customer_obj.balance += amount
                if amount > 0:
                    print(f"${amount:.2f} deposited successfully!")
                    print(f"New Balance: ${customer_obj.balance:.2f}")
            else:
                print("Please create an account first!")
        elif choice == '4':
            if customer_obj:
                amount = account.withdraw(customer_obj)
                customer_obj.balance -= amount
                if amount > 0:
                    print(f"${amount:.2f} withdrawn successfully!")
            else:
                print("Please create an account first!")
        elif choice == '5':
            is_running = False
        else:
            print("That is not a valid choice")
            
    print("Thank you! Have a nice day!")

if __name__ == '__main__':
    main()