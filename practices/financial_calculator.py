# LL 6th Period Finance Calculator
def calculate_budget(income, rent, utilities, groceries):
    return income - rent - utilities - groceries


income = float(input("Enter your monthly income: "))
rent = float(input("Enter your monthly rent: "))
utilities = float(input("Enter your monthly utilities: "))
groceries = float(input("Enter your monthly groceries: "))
remaining_funds = calculate_budget(income, rent, utilities, groceries)



print(f"Your Monthly Budget is {remaining_funds} ")
print("Total income: $", income)
print("Total expenses: $", rent + utilities + groceries)
