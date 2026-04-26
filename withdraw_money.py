from utils import *

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