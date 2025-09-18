# LL 6th Period Finance Calculator

# Get monthly income and expenses as input from the user and convert to floats
try:
    income = float(input("What is your monthly income: "))
    rent = float(input("What is your monthly rent/mortgage: "))
    utilities = float(input("What is your monthly utilities: "))
    groceries = float(input("What is your monthly groceries: "))
    transportation = float(input("What is your monthly transportation: "))
except ValueError:
    print("Invalid input. Please enter numbers only.")
    exit()

# Set savings goal (10% of monthly income)
savings_goal = income * 0.10

# Calculate total expenses
total_expenses = rent + utilities + groceries + transportation

# Calculate remaining spending money
spending_money = income - total_expenses - savings_goal

# Function to calculate percentage of income for each category
def calculate_percentage(amount, total_income):
    if total_income == 0:
        return 0
    return (amount / total_income) * 100

# Calculate percentages for each expense and savings
rent_percent = calculate_percentage(rent, income)
utilities_percent = calculate_percentage(utilities, income)
groceries_percent = calculate_percentage(groceries, income)
transportation_percent = calculate_percentage(transportation, income)
savings_percent = calculate_percentage(savings_goal, income)

# Output results, formatted to two decimal places for currency and rounded percentages
print(f"Your rent is ${rent:,.2f} and that is {rent_percent:.0f}% of your income.")
print(f"Your utilities are ${utilities:,.2f} and that is {utilities_percent:.0f}% of your income.")
print(f"Your groceries are ${groceries:,.2f} and that is {groceries_percent:.0f}% of your income.")
print(f"Your transportation is ${transportation:,.2f} and that is {transportation_percent:.0f}% of your income.")
print(f"You should save ${savings_goal:,.2f} a month, that is {savings_percent:.0f}% of your income.")
print(f"You have ${spending_money:,.2f} of spending money each month!")
