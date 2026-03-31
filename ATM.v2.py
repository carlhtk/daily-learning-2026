def display_menu():
    print("\n======================")
    print("     ATM MACHINE V2     ")
    print("========================")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. View Transaction History")
    print("5. Exit")
    print("========================")

def deposit(current_balance, amount):
    return current_balance + amount

def withdraw(current_balance, amount):
    if amount <= current_balance:
        return current_balance - amount
    else: 
        return None
    

balance = 1000.00
transaction_history = []
option = 0 

while option != 5:
    display_menu()

    try:
        option = int(input("Select and option (1-5): "))
        if option == 1:
           print(f"Current balance: ${balance:.2f}")

        elif option == 2:
            amount = float(input("Enter deposit amount: $"))
            if amount > 0:
                balance = deposit(balance, amount)
                transaction_history.append(f"Deposit: =${amount:.2f}")
                print("Deposit successful.")
            else:
                print("Invalid amount.")
        
        elif option == 3:
            amount = float(input("Enter withdrawal amount: $"))
            if amount > 0:
                new_balance = withdraw(balance, amount)
                if new_balance is not None:
                    balance = new_balance
                    transaction_history.append(f"withdrawal: -${amount:.2f}")
                    print("Withdrawal successful.")
                else:
                    print("Invalid amount.")
        
        elif option == 4:
            print("\n--- TRANSACTION HISTORY ---")
            if not transaction_history:
                print("No transactions yet.")
            else:
                for record in transaction_history:
                    print(record)

        elif option == 5:
            print("Thank you for using our ATM. Goodbye.")

        else:
            print("Invalid option.")

    except ValueError:
        print("Error: Please enter numbers only.")
