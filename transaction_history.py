from utils import *


# -----SHOW TRANSACTION HISTORY-----
def show_transactions():
    if not transactions:
        print("No transactions yet.")
    else:
        print("\n--- Transaction History ---")
        for t in transactions:
            print(t)