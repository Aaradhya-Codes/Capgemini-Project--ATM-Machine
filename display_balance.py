import utils

def display_balance():
    print("\n" + "─" * 40)
    print("CURRENT BALANCE")
    print("─" * 40)
    print(f"₹ {utils.balance:.2f}")
    print("─" * 40)
