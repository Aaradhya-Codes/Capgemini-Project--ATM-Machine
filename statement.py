import utils

def statement():
    print("\n" + "═" * 55)
    print("                 ACCOUNT STATEMENT")
    print("═" * 55)

    if not utils.transactions:
        print("No transactions found.")
        print("═" * 55)
        return

    print(f"  {'#':<4} {'Type':<12} {'Amount':>12}  {'Balance After':>14}")
    print("  " + "─" * 51)

    for i, txn in enumerate(utils.transactions, start=1):
        print(
            f"  {i:<4} {txn['type']:<12} "
            f"₹ {txn['amount']:>10.2f}  "
            f"₹ {txn['balance_after']:>12.2f}"
        )

    print("═" * 55)
    print(f"  Total Transactions : {len(utils.transactions)}")
    print(f"  Current Balance    : ₹ {utils.balance:.2f}")
    print("═" * 55)
