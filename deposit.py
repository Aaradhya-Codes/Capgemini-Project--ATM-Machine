import utils
from utils import _record

def deposit():
    print("\n" + "─" * 40)
    print("DEPOSIT MONEY")
    print("─" * 40)

    amount = float(input("Enter amount to deposit : ₹"))

    if amount <= 0:
        print("\nAmount must be greater than ₹0.")
        return

    utils.balance += amount
    _record("Deposit", amount)

    print(f"\n₹ {amount:.2f} deposited successfully.")
    print(f"Updated Balance : ₹ {utils.balance:.2f}")
    print("─" * 40)
