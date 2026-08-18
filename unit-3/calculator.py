"""
Multi-Function Calculator
A calculator that performs arithmetic operations on two numbers.
"""

def main():
    """
    Main function to run the calculator.
    """
    # Get two numbers using float(input())
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Calculate operations
    addition = round(num1 + num2, 2)
    subtraction = round(num1 - num2, 2)
    multiplication = round(num1 * num2, 2)
    
    # Division with error handling
    if num2 != 0:
        division = round(num1 / num2, 2)
        floor_division = round(num1 // num2, 2)
        modulus = round(num1 % num2, 2)
        
        # Display results
        print(f"\n{'Operation':<20} {'Result'}")
        print("-"*40)
        print(f"{'Addition':<20} {addition}")
        print(f"{'Subtraction':<20} {subtraction}")
        print(f"{'Multiplication':<20} {multiplication}")
        print(f"{'Division':<20} {division}")
        print(f"{'Floor Division':<20} {floor_division}")
        print(f"{'Modulus':<20} {modulus}")
    else:
        # Display results with error for division
        print(f"\n{'Operation':<20} {'Result'}")
        print("-"*40)
        print(f"{'Addition':<20} {addition}")
        print(f"{'Subtraction':<20} {subtraction}")
        print(f"{'Multiplication':<20} {multiplication}")
        print(f"{'Division':<20} Error: Cannot divide by zero")
        print(f"{'Floor Division':<20} Error: Cannot divide by zero")
        print(f"{'Modulus':<20} Error: Cannot divide by zero")


# Entry point of the program
if __name__ == "__main__":
    main()
