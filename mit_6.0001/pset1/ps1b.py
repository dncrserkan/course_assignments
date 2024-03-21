annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to saved, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

portion_down_payment = 0.25 * total_cost
current_savings = 0
rate = 0.04    # annual rate for savings
number_of_months = 0

while current_savings < portion_down_payment:
    if number_of_months % 6 == 0 and number_of_months != 0:
        annual_salary += annual_salary*semi_annual_raise
        
    current_savings += (current_savings * rate / 12) + (annual_salary * portion_saved / 12)
    number_of_months += 1

print("Number of months: " + str(number_of_months))
