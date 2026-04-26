from utils import *

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