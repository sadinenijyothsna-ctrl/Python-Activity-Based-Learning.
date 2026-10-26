# Manufacturing Cost and Profitability Analysis

product_name = "School Bags"

material_cost = 120
labour_cost = 30
machine_cost = 10
selling_price = 200
profit_target = 3000

# Five test cases
test_quantities = [100, 50, 75, 25, 150]

for quantity in test_quantities:
    total_material_cost = quantity * material_cost
    total_labour_cost = quantity * labour_cost
    total_machine_cost = quantity * machine_cost

    total_cost = (
        total_material_cost
        + total_labour_cost
        + total_machine_cost
    )

    total_revenue = quantity * selling_price
    profit = total_revenue - total_cost

    print("\nProduct Name:", product_name)
    print("Quantity:", quantity)
    print("Total Manufacturing Cost:", total_cost)
    print("Total Sales Revenue:", total_revenue)
    print("Profit:", profit)

    if profit >= profit_target:
        print("Profit Target: Achieved")
    else:
        print("Profit Target: Not Achieved")

    print("-" * 35)



