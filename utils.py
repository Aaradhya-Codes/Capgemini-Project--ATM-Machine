balance = 10_000.00
transactions = []

def _record(txn_type: str, amount: float):
    transactions.append({
        "type":          txn_type,
        "amount":        amount,
        "balance_after": balance,
    })
