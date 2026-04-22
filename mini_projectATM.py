balance = 0
transactions = []   


# -----SHOW BALANCE-----
def show_balance(balance):
    print(f"Your Balance is ₹{balance}")


# -----DEPOSIT MONEY-----
def dep_amount(balance):
    amount = float(input("Enter amount to deposit: "))

    if amount > 0:
        balance += amount
        transactions.append(f"Deposited ₹{amount}")
        print("Amount Deposited Successfully!")
    else:
        print("Invalid Amount!")

    return balance  


# -----WITHDRAW MONEY-----
def withdraw_amount(balance):
    amount = float(input("Enter amount to withdraw: "))

    if amount > balance:
        print("Insufficient Balance!")
    elif amount <= 0:
        print("Invalid Amount!")
    else:
        balance -= amount
        transactions.append(f"Withdrew ₹{amount}")
        print("Withdrawal Successful!")

    return balance


# -----SHOW TRANSACTION HISTORY-----
def show_transactions():
    if not transactions:
        print("No transactions yet.")
    else:
        print("\n--- Transaction History ---")
        for t in transactions:
            print(t)


# -----MAIN-----
def atm():
    global balance
    while True:
        print("\n----Banking ATM Simulation----")
        print("1. Show Balance")
        print("2. Deposit Amount")
        print("3. Withdraw Amount")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance = dep_amount(balance)
        elif choice == "3":
            balance = withdraw_amount(balance)
        elif choice == "4":
            show_transactions()
        elif choice == "5":
            print("Thank you for using ATM!")
            break
        else:
            print("Invalid choice")

atm()

        

