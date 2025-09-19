# LL 6th Period Finance Calculator

income = float(input("Enter your monthly income: "))
rent = float(input("Enter your monthly rent: "))
utilities = float(input("Enter your monthly utilities: "))
groceries = float(input("Enter your monthly groceries: "))
remaining_funds = income - rent - utilities - groceries

print(f"Your Monthly Budget is {remaining_funds} ")
print("Total income: $", income)
print("Total expenses: $", rent + utilities + groceries)
