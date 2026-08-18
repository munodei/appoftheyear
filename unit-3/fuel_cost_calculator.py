"""
South African Fuel Cost Calculator
A quick calculator for estimating travel fuel costs.
"""

def main():
    """
    Main function to run the fuel cost calculator.
    """
    # Step 1: Ask for kilometers to drive
    kilometers = float(input("How many kilometers do you want to drive? "))
    
    # Step 2: Ask for current petrol price
    petrol_price = float(input("Enter the current petrol price per liter (e.g., 22.45): R"))
    
    # Step 3: Calculate liters needed (1 liter per 10 km)
    liters_needed = kilometers / 10
    
    # Step 4: Calculate total cost
    total_cost = liters_needed * petrol_price
    
    # Step 5: Round and display the result
    total_cost_rounded = round(total_cost, 2)
    
    print(f"\nDistance: {kilometers} km")
    print(f"Fuel needed: {round(liters_needed, 2)} liters")
    print(f"Total cost: R{total_cost_rounded}")


# Entry point of the program
if __name__ == "__main__":
    main()
