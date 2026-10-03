print ("Welcome to the Sherwin-Williams goal tracker v1.0")
def get_dollar_amount(prompt):
    while True:
        try:
            amount = float(input(prompt))
            if amount < 0:
                print("Please enter $0 or more.")
            else:
                return amount
        except ValueError:
            print("Please enter a valid number, such as 25000.")


def sales_coach(monthly_data, yearly_budget, yearly_actual_sales):
    print("\n----- SALES COACH -----")
    print("Ask about yearly totals, your best month, or your worst month.")
    print("Type 'help' for examples or 'quit' to leave the coach.")

    while True:
        question = input("\nYou: ").lower()

        if question == "quit":
            print("Coach: Keep up the great work!")
            break

        elif "year" in question or "total" in question or "budget" in question:
            difference = yearly_actual_sales - yearly_budget

            print(f"Coach: Your yearly budget is ${yearly_budget:,.2f}.")
            print(f"Coach: Your yearly actual sales are ${yearly_actual_sales:,.2f}.")

            if difference >= 0:
                print(f"Coach: You are ${difference:,.2f} above budget.")
            else:
                print(f"Coach: You are ${abs(difference):,.2f} below budget.")

        elif "best" in question:
            best_month = max(
                monthly_data,
                key=lambda month: monthly_data[month]["actual_sales"]
            )
            sales = monthly_data[best_month]["actual_sales"]
            budget = monthly_data[best_month]["budget"]

            print(f"Coach: Your best sales month was {best_month}.")
            print(f"Coach: Actual sales were ${sales:,.2f} against a ${budget:,.2f} budget.")

        elif "worst" in question or "lowest" in question:
            lowest_month = min(
                monthly_data,
                key=lambda month: monthly_data[month]["actual_sales"]
            )
            sales = monthly_data[lowest_month]["actual_sales"]
            budget = monthly_data[lowest_month]["budget"]

            print(f"Coach: Your lowest sales month was {lowest_month}.")
            print(f"Coach: Actual sales were ${sales:,.2f} against a ${budget:,.2f} budget.")

        elif "help" in question:
            print("Coach: You can ask:")
            print("  - How is my yearly total?")
            print("  - What was my best month?")
            print("  - What was my worst month?")

        else:
            print("Coach: I can help with yearly totals, best month, and worst month.")
            print("Coach: Type 'help' to see example questions.")


# Overall goal tracker
goal = get_dollar_amount("What is your overall goal? $")
current = get_dollar_amount("How much have you completed? $")

remaining = goal - current
percentage = (current / goal) * 100 if goal > 0 else 0

bar_length = 20
filled = min(int((percentage / 100) * bar_length), bar_length)
progress_bar = "#" * filled + "-" * (bar_length - filled)

print("\n----- OVERALL GOAL SUMMARY -----")
print(f"Goal:      ${goal:,.2f}")
print(f"Completed: ${current:,.2f}")
print(f"Progress:  {percentage:.2f}%")
print(f"[{progress_bar}]")

if remaining > 0:
    print(f"Remaining: ${remaining:,.2f}")
else:
    print(f"Over Goal: ${abs(remaining):,.2f}")
    print("Goal reached—great work!")

# Monthly budget and actual-sales tracker
months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

monthly_data = {}

print("\n----- ENTER MONTHLY BUDGET AND ACTUAL SALES -----")

for month in months:
    print(f"\n{month}")
    budget = get_dollar_amount("Monthly budget: $")
    actual_sales = get_dollar_amount("Actual sales: $")

    monthly_data[month] = {
        "budget": budget,
        "actual_sales": actual_sales
    }

yearly_budget = 0
yearly_actual_sales = 0

print("\n----- YEARLY SALES SUMMARY -----")

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

# Start the chatbot
sales_coach(monthly_data, yearly_budget, yearly_actual_sales)