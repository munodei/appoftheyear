def get_user_input():
    """
    Collect personal information from the user.
    
    Returns:
        tuple: Contains first name, surname, age, and favourite number
    """
    # Get string inputs for name
    first_name = input("Enter your first name: ")
    surname = input("Enter your surname: ")
    
    # Get integer input for age
    while True:
        try:
            age = int(input("Enter your age: "))
            break
        except ValueError:
            print("Please enter a valid integer for age.")
    
    # Get float input for favourite number
    while True:
        try:
            favourite_number = float(input("Enter your favourite number: "))
            break
        except ValueError:
            print("Please enter a valid number.")
    
    return first_name, surname, age, favourite_number


def format_profile_card(first_name, surname, age, favourite_number):
    # Combine first name and surname to create full name
    full_name = f"{first_name} {surname}"
    
    # Calculate age in months
    age_in_months = age * 12
    
    # Round favourite number to 2 decimal places
    rounded_number = round(favourite_number, 2)
    
    # Display the profile card
    print("\n" + "="*50)
    print("STUDENT PROFILE CARD")
    print("="*50)
    
    # Display formatted greeting
    print(f"\nWelcome, {full_name}!")
    
    # Display name transformations
    print(f"\nName Formats:")
    print(f"   UPPERCASE: {full_name.upper()}")
    print(f"   Title Case: {full_name.title()}")
    
    # Display age information
    print(f"\nAge Information:")
    print(f"   Age: {age} years")
    print(f"   Age in months: {age_in_months} months")
    
    # Display favourite number information
    print(f"\nFavourite Number:")
    print(f"   Original: {favourite_number}")
    print(f"   Rounded (2 decimal places): {rounded_number}")
    
    # Display data types
    print(f"\nData Types:")
    print(f"   First name: {type(first_name).__name__}")
    print(f"   Surname: {type(surname).__name__}")
    print(f"   Age: {type(age).__name__}")
    print(f"   Favourite number: {type(favourite_number).__name__}")
    
    print("\n" + "="*50)


def main():
    """
    Main function to orchestrate the program flow.
    """
    # Get user input
    first_name, surname, age, favourite_number = get_user_input()
    
    # Display formatted profile card
    format_profile_card(first_name, surname, age, favourite_number)


# Entry point of the program
if __name__ == "__main__":
    main()
