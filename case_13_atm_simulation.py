# ATM Transaction Sequence Simulation
balance = 5000
withdrawal_limit = 3000

transactions = [
    ("Deposit", 1000),
    ("Withdraw", 2000),
    ("Withdraw", 4000),
    ("Deposit", 500),
    ("Withdraw", -200)
]

total_deposits = 0
total_withdrawals = 0
successful = 0
rejected = 0

print("ATM TRANSACTION SUMMARY")
print("Starting Balance: Rs.", balance)
print("-" * 35)

for transaction, amount in transactions:
    print("\nTransaction:", transaction)
    print("Amount: Rs.", amount)

    if amount <= 0:
        print("Status: Rejected - Invalid amount")
        rejected += 1

    elif transaction == "Deposit":
        balance += amount
        total_deposits += amount
        successful += 1
        print("Status: Successful")

    elif transaction == "Withdraw":
        if amount > withdrawal_limit:
            print("Status: Rejected - Exceeds withdrawal limit")
            rejected += 1
        elif amount > balance:
            print("Status: Rejected - Insufficient balance")
            rejected += 1
        else:
            balance -= amount
            total_withdrawals += amount
            successful += 1
            print("Status: Successful")

    print("Current Balance: Rs.", balance)

print("\n" + "=" * 35)
print("FINAL TRANSACTION SUMMARY")
print("Total Deposits: Rs.", total_deposits)
print("Total Withdrawals: Rs.", total_withdrawals)
print("Successful Transactions:", successful)
print("Rejected Transactions:", rejected)
print("Final Balance: Rs.", balance)
