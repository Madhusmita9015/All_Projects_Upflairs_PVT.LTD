# ATM Simulation Project
correct_pin = "0123"
balance = 10000
for attempt in range(3):
    pin = int(input("Enter your 4-digit PIN: "))
    if pin == correct_pin:
        print(" Access Granted!")
        break
    else:
        print("Incorrect PIN.")
else:
    print("Too many incorrect attempts. Exiting.")
    exit()

while True:
    print("\n---- ATM Menu ----")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        print(f"Your current balance is ₹{balance}")
    
    elif choice == "2":
        amount = float(input("Enter amount to deposit: ₹"))
        if amount > 0:
            balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid amount.")
    
    elif choice == "3":
        amount = float(input("Enter amount to withdraw: ₹"))
        if amount <= balance and amount > 0:
            balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance or invalid amount.")
    
    elif choice == "4":
        print("Thank you for using the ATM. Goodbye!")
        break
    
    else:
        print("Invalid option. Please choose between 1 and 4.")
