# --- FUNCTIONS ---

def display_menu():
    print("\n==========================")
    print("       ATM MACHINE        ")
    print("==========================")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    print("==========================")

def deposit(current_balance, amount):
    """Adds the amount to the balance and returns the new total."""
    new_balance = current_balance + amount
    return new_balance

def withdraw(current_balance, amount):
    """Subtracts the amount if funds are available; otherwise, warns the user."""
    if amount <= current_balance:
        new_balance = current_balance - amount
        print(f"Successful withdrawal: ${amount:.2f}")
        return new_balance
    else:
        print("Error: Insufficient funds for this withdrawal.")
        return current_balance



balance = 1000.0  
option = 0

while option != 4:
    display_menu()
    
    try:
        option = int(input("Select an option (1-4): "))
        
        if option == 1:
            print(f"Your current balance is: ${balance:.2f}")
            
        elif option == 2:
            dep_amount = float(input("Enter amount to deposit: $"))
            if dep_amount > 0:
                balance = deposit(balance, dep_amount)
                print(f"Deposit completed. Current balance: ${balance:.2f}")
            else:
                print("Amount must be greater than 0.")
                
        elif option == 3:
            withdraw_amount = float(input("Enter amount to withdraw: $"))
            if withdraw_amount > 0:
                balance = withdraw(balance, withdraw_amount)
            else:
                print("Amount must be greater than 0.")
                
        elif option == 4:
            print("Thank you for using our ATM. Have a great day.")
            
        else:
            print("Invalid option, please try again.")
            
    except ValueError:
        print("Error: Please enter numbers only.")