import utils
from utils import _record

def withdraw():
    print("\n" + "─" * 40)
    print("WITHDRAW MONEY")
    print("─" * 40)

    amount = float(input("Enter amount to withdraw : ₹ "))

    if amount <= 0:
        print("\nAmount must be greater than ₹ 0.")
        return

    elif amount > utils.balance:
        print(f"\nInsufficient balance!")
        print(f"Available Balance : ₹ {utils.balance:.2f}")
        return

    utils.balance -= amount
    _record("Withdrawal", amount)

    print(f"\n₹ {amount:.2f} withdrawn successfully.")
    print(f"Remaining Balance : ₹ {utils.balance:.2f}")
    print("─" * 40)
