# ATM Machine with login using lists, tuples, and dictionaries

# Initialize account balances and PINs
account_info = {
    'islam': {'balance': 5000, 'pin': '1234'},
    'negm': {'balance': 3500, 'pin': '5678'},
    'kenawy': {'balance': 2000, 'pin': '9101'}
}

# Main program
while True:
    print("\nWelcome to MyBank ATM!")
    name = input("Enter account holder name: ")
    if name not in account_info:
        print("Invalid account holder name. Please try again.")
        continue

    pin = input("Enter PIN: ")
    if pin != account_info[name]['pin']:
        print("Invalid PIN. Please try again.")
        continue

    print("Login successful.")

    while True:
        print("\nATM Menu:")
        print("1. Check balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Logout")

        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            print(f"Account balance for {name}: {account_info[name]['balance']}")

        elif choice == 2:
            amount = int(input("Enter amount to withdraw: "))
            if amount > account_info[name]['balance']:
                print("Insufficient balance")
            else:
                account_info[name]['balance'] -= amount
                print(f"Withdrawal successful. New balance for {name}: {account_info[name]['balance']}")

        elif choice == 3:
            amount = int(input("Enter amount to deposit: "))
            account_info[name]['balance'] += amount
            print(f"Deposit successful. New balance for {name}: {account_info[name]['balance']}")

        elif choice == 4:
            print("Logout successful.")
            break

        else:
            print("Invalid choice. Please try again.")
    break