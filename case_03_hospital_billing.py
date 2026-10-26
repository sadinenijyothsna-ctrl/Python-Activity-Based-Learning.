consultation = float(input("Enter consultation charge: "))
diagnostic = float(input("Enter diagnostic charge: "))
treatment = float(input("Enter treatment charge: "))

if consultation < 0 or diagnostic < 0 or treatment < 0:
    print("Invalid charges")
else:
    total = consultation + diagnostic + treatment

    if total >= 5000:
        concession = total * 10 / 100
    else:
        concession = 0

    final_bill = total - concession

    if final_bill < 2000:
        category = "Low Bill"
    elif final_bill < 10000:
        category = "Medium Bill"
    else:
        category = "High Bill"

    print("Total bill:", total)
    print("Concession:", concession)
    print("Final bill:", final_bill)
    print("Category:", category)