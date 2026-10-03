print ("Welcome to the Sherwin-Williams goal tracker")
goal = float(input("What is your goal?"))
current = float(input("How much have you completed? $"))

if goal <= 0:
    print("Your goal must be greater than $0.")
else:
    remaining = goal - current
    percentage = (current / goal) * 100

    bar_length = 20
    filled = min(int((percentage / 100) * bar_length), bar_length)
    progress_bar = "#" * filled + "-" * (bar_length - filled)

    print()
    print("----- CURRENT GOAL SUMMARY -----")
    print(f"Goal:      ${goal:,.2f}")
    print(f"Completed: ${current:,.2f}")
    print(f"Progress:  {percentage:.2f}%")
    print(f"[{progress_bar}]")

    if remaining > 0:
        print(f"Remaining: ${remaining:,.2f}")
    else:
        print(f"Over goal: ${abs(remaining):,.2f}")
        print("Goal reached—great work!")

    monthly_data = {}
    months = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ]

    print()
    print("----- ENTER MONTHLY BUDGET AND ACTUAL SALES -----")

    for month in months:
        budget = float(input(f"{month} monthly budget: $"))
        actual_sales = float(input(f"{month} actual sales: $"))

        monthly_data[month] = {
            "budget": budget,
            "actual_sales": actual_sales
        }

    yearly_budget = 0
    yearly_actual_sales = 0

    print()
    print("----- YEARLY SALES SUMMARY -----")

    for month, data in monthly_data.items():
        budget = data["budget"]
        actual_sales = data["actual_sales"]
        difference = actual_sales - budget

        yearly_budget += budget
        yearly_actual_sales += actual_sales

        print(f"\n{month}")
        print(f"  Budget:       ${budget:,.2f}")
        print(f"  Actual Sales: ${actual_sales:,.2f}")

        if difference >= 0:
            print(f"  Above Budget: ${difference:,.2f}")
        else:
            print(f"  Below Budget: ${abs(difference):,.2f}")

    yearly_difference = yearly_actual_sales - yearly_budget

    print("\n----- YEARLY TOTALS -----")
    print(f"Yearly Budget:       ${yearly_budget:,.2f}")
    print(f"Yearly Actual Sales: ${yearly_actual_sales:,.2f}")

    if yearly_difference >= 0:
        print(f"Yearly Above Budget: ${yearly_difference:,.2f}")
    else:
        print(f"Yearly Below Budget: ${abs(yearly_difference):,.2f}")