# Tuple-Based Transaction Audit
transactions = [
    (101, 500, "Deposit"),
    (102, 1000, "Withdraw"),
    (103, -200, "Deposit"),
    (102, 300, "Deposit"),
    (104, 700, "Withdraw")
]
seen_ids = []
valid_count = 0
invalid_count = 0
duplicate_count = 0
print("TUPLE-BASED TRANSACTION AUDIT")
print("-" * 40)
for transaction in transactions:
    transaction_id, amount, transaction_type = transaction
    print("\nTransaction ID:", transaction_id)
    print("Amount: Rs.", amount)
    print("Type:", transaction_type)
    if transaction_id in seen_ids:
        print("Status: Duplicate Transaction ID")
        duplicate_count += 1
    elif amount <= 0:
        print("Status: Invalid Amount")
        invalid_count += 1
        seen_ids.append(transaction_id)
    elif transaction_type not in ("Deposit", "Withdraw"):
        print("Status: Invalid Transaction Type")
        invalid_count += 1
        seen_ids.append(transaction_id)
    else:
        print("Status: Valid Transaction")
        valid_count += 1
        seen_ids.append(transaction_id)
print("\n" + "-" * 40)
print("Valid Transactions:", valid_count)
print("Invalid Transactions:", invalid_count)
print("Duplicate Transactions:", duplicate_count)
print("Total Transactions:", len(transactions))
