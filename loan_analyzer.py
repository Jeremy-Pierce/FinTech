# coding: utf-8
import csv
from pathlib import Path

# Automate the calculations for the loan portfolio summaries.

loan_costs = [500, 600, 200, 1000, 450]

# Calculating & printing the total number of loans
total_number_of_loans = len(loan_costs)
print(f"There are {total_number_of_loans} loans total")

# Calculating & printing the sum of all the loans
total_value_of_all_loans = sum(loan_costs)
print(f"The total value of all the loans is ${total_value_of_all_loans}")

# Calculating & printing the average loan price
average_loan_price = (total_value_of_all_loans / total_number_of_loans)
print(f"The average loan price is ${average_loan_price}")

'''
2. Use the formula for Present Value to calculate a "fair value" of the loan. Use a minimum required return of 20% as the discount rate.
3. Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
    a. If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
    b. Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.

    @NOTE:
    If Present Value represents the loan's fair value (given the required minimum return of 20%), does it make sense to buy the loan at its current cost?
'''
# Given the following loan data, you will need to calculate the present value for the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}
# Used the get() on the dictionary of additional information to extract the Future Value and Remaining Months on the loan.
for future_value in loan:
    future_value = loan["future_value"]
print(future_value)

for remaining_months in loan:
    remaining_months = loan["remaining_months"]
print(remaining_months)

for loan_price in loan:
    loan_price = loan["loan_price"]
print(loan_price)

annual_discount_rate = .20

present_value = (future_value) / (1+ annual_discount_rate/12)**(remaining_months)
if present_value >= loan_price:
    print("The present value of the loan is worth at least the cost to purchase it")
else:
    print("The present value of the loan is too expensive and not worth the price")
print(f"{present_value: .2f}")


# Given the following loan data, calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}
for future_value in new_loan:
    future_value = new_loan["future_value"]
print(future_value)

for remaining_months in new_loan:
    remaining_months = loan["remaining_months"]
print(remaining_months)

for loan_price in new_loan:
    loan_price = new_loan["loan_price"]
print(loan_price)
annual_discount_rate = .20

def calculate_present_value(future_value, annual_discount_rate, remaining_months):
    present_value = (future_value) / (1+ annual_discount_rate/12)**(remaining_months)
    return present_value

calculate_present_value(future_value, annual_discount_rate, remaining_months)
print(f"The present value of the loan is: {present_value}")


"""Part 4: Conditionally filter lists of loans.

In this section, you will use a loop to iterate through a series of loans and select only the inexpensive loans.

1. Create a new, empty list called `inexpensive_loans`.
2. Use a for loop to select each loan from a list of loans.
    a. Inside the for loop, write an if-statement to determine if the loan_price is less than or equal to 500
    b. If the loan_price is less than or equal to 500 then append that loan to the `inexpensive_loans` list.
3. Print the list of inexpensive_loans.
"""
loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# @TODO: Create an empty list called `inexpensive_loans`
inexpensive_loans = []:
    

# @TODO: Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
for future_value in loans:
    future_value = loans["future_value"]
print(future_value)

for remaining_months in loans:
    remaining_months = loans["remaining_months"]
print(remaining_months)

for loan_price in loans:
    loan_price = loans["loan_price"]
print(loan_price)
if present_value 
# @TODO: Print the `inexpensive_loans` list
# YOUR CODE HERE!


"""Part 5: Save the results.

Output this list of inexpensive loans to a csv file
    1. Use `with open` to open a new CSV file.
        a. Create a `csvwriter` using the `csv` library.
        b. Use the new csvwriter to write the header variable as the first row.
        c. Use a for loop to iterate through each loan in `inexpensive_loans`.
            i. Use the csvwriter to write the `loan.values()` to a row in the CSV file.

    Hint: Refer to the official documentation for the csv library.
    https://docs.python.org/3/library/csv.html#writer-objects

"""

# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")

# @TODO: Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
# YOUR CODE HERE!
 # save my changes
