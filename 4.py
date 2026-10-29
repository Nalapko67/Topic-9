import math
print("Two-Digit Number Analysis")
number = int(input("Enter a two-digit number: "))
abs_number = abs(number)
if 10 <= abs_number <= 99:
    tens = abs_number // 10
    units = abs_number % 10
    digit_sum = tens + units
    digit_product = tens * units
    print(f"Number of tens: {tens}")
    print(f"Number of units: {units}")
    print(f"Sum of digits: {digit_sum}")
    print(f"Product of digits: {digit_product}")
else:
    print("Error: The entered number is not a two-digit number!") 