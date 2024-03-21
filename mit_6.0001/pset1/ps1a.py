annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to saved, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

portion_down_payment = 0.25 * total_cost
current_savings = 0.0
rate = 0.04    # annual rate for savings
number_of_months = 0

while current_savings < portion_down_payment:
    current_savings += (current_savings * rate / 12) + (annual_salary * portion_saved / 12)
    number_of_months += 1

print("Number of months: " + str(number_of_months))
