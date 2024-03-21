annual_salary = int(input("Enter the starting salary: "))
annual_salary_temp = annual_salary      # Need a temp value because it must be reset for every new guesses
semi_annual_raise = 0.07                # Raise in every six months

total_cost = 1000000                    # Given in pset as $1M
portion_down_payment = 0.25             # Given in pset as 25%
down_payment = total_cost * portion_down_payment

current_savings = 0     # Set initial saving to $0
rate = 0.04             # Annual return for savings - Given in pset as 4%
number_of_months = 36   #  Given in pset as 3 years


"""Because we are searching for a value that is in principle a float, we are going to limit ourselves to two
decimals of accuracy (i.e., we may want to save at 7.04% or 0.0704 in decimal - but we are not
going to worry about the difference between 7.041% and 7.039%). This means we can search for an
integer between 0 and 10000 (using integer division), and then convert it to a decimal percentage
(using float division) to use when we are calculating the current_savings after 36 months. By using
this range, there are only a finite number of numbers that we are searching over, as opposed to the
infinite number of decimals between 0 and 1. This range will help prevent infinite loops. The reason we
use 0 to 10000 is to account for two additional decimal places in the range 0% to 100%. Your code
should print out a decimal (e.g. 0.0704 for 7.04%)."""


epsilon = 100   # Acceptaple range - simply savings wanted to be within $100 of the required down_payment
high = 10000    # 100% but in simplicity we multipy it by 100
low = 0         # 0%
steps = 1       # Number of bisection search
guess = (low + high) // 2   # Percentage of user annual earnings to investment


while abs(down_payment - current_savings) >= epsilon:

    # Calculate the total saving end of the number_of_months
    for i in range(1, number_of_months+1):
        current_savings += (current_savings * rate / 12) + (annual_salary_temp * guess / (12 * 10000))
        if i % 6 == 0:
            annual_salary_temp += annual_salary_temp * semi_annual_raise

    # Check if user is within acceptable range. If so, print results
    if abs(down_payment - current_savings) <= epsilon:
        # See, how it works step by step
        print(steps, "\t g:", guess/10000, "\t dp:", down_payment, "\t cs:", int(current_savings))

        print(f"Best savings rate: {(guess/10000):.4f}")
        print(f"Steps in bisection search: {steps}")
        break

    # See, how it works step by step
    print(steps, "\t g:", guess/10000, "\t dp:", down_payment, "\t cs:", int(current_savings))

    # Above condition did not met, set new guess
    if down_payment > current_savings:
        low = guess
    else:
        high = guess

    if guess >= 9999:
        print("It is not possible to pay the down payment in three years.")
        break
    if guess <= 100:
        print("heyyy, you are rich")
        break

    guess = (low + high) // 2
    current_savings = 0
    annual_salary_temp = annual_salary
    steps += 1
    
    if steps > 30:
        break
