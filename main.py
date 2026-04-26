
from utils import *
from show_balance import * 
from withdraw_money import *
from deposit_money import *
from transaction_history import *


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

        

