#Create two Python scripts: robust_division_calculator.py, which contains the division logic including error handling,
# and main.py, which interfaces with the user through the command line.

def safe_divide(numerator, denominator):
    try:
        result = numerator/denominator
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter numeric values only.")
    else:
        print(f"The result of the division is {result:.2f}")
    finally:
        print("Execution of the divide_numbers function is complete.")
