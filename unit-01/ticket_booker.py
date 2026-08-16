def get_booking_details():
    """
    Collect booking information from the user.
    
    Returns:
        tuple: Contains customer name and artist/band name
    """
    # Get customer name from user
    customer_name = input("Enter your full name: ").strip()
    
    # Get artist/band name from user
    artist_name = input("Enter the name of the band/artist you want to see: ").strip()
    
    return customer_name, artist_name


def validate_booking_details(customer_name, artist_name):
    """
    Validate that the booking details are not empty.
    
    Args:
        customer_name (str): The customer's name
        artist_name (str): The artist/band name
    
    Returns:
        bool: True if both fields are non-empty, False otherwise
    """
    # Check if both fields contain text
    if not customer_name or not artist_name:
        print("\nError: Both name and artist fields must be filled in.")
        print("Please try again.\n")
        return False
    return True


def display_booking_confirmation(customer_name, artist_name):
    """
    Display the personalized booking confirmation message.
    
    Args:
        customer_name (str): The customer's name
        artist_name (str): The artist/band name
    """
    # Create a formatted booking confirmation
    print("\n" + "="*60)
    print("CONCERT TICKET BOOKING CONFIRMATION")
    print("="*60)
    
    # Display personalized confirmation message
    print(f"\nHey {customer_name}! Your tickets to see {artist_name} are booked successfully!")
    
    # Additional booking details for better user experience
    print("\nBooking Details:")
    print(f"   Customer Name: {customer_name.title()}")
    print(f"   Artist/Band: {artist_name.title()}")
    print(f"   Event Status: CONFIRMED")
    print(f"   Booking Reference: BTC-{abs(hash(customer_name + artist_name)) % 100000:05d}")
    
    print("\n" + "="*60)
    print("Thank you for using the Concert Ticket Booker!")
    print("A confirmation email will be sent to your registered email address.")


def display_booking_summary(customer_name, artist_name):
    """
    Display a summary of the booking information and data types.
    
    Args:
        customer_name (str): The customer's name
        artist_name (str): The artist/band name
    """
    # Display data type information for educational purposes
    print("\n" + "-"*60)
    print("BOOKING SYSTEM INFORMATION")
    print("-"*60)
    print(f"   Customer Name Data Type: {type(customer_name).__name__}")
    print(f"   Artist Name Data Type: {type(artist_name).__name__}")
    print(f"   Customer Name Length: {len(customer_name)} characters")
    print(f"   Artist Name Length: {len(artist_name)} characters")
    print("-"*60)


def format_name_display(customer_name, artist_name):
    """
    Demonstrate different string formatting options for the names.
    
    Args:
        customer_name (str): The customer's name
        artist_name (str): The artist/band name
    
    Returns:
        tuple: Contains formatted versions of the names
    """
    # Create different formatting variations
    customer_name_upper = customer_name.upper()
    customer_name_title = customer_name.title()
    artist_name_upper = artist_name.upper()
    artist_name_title = artist_name.title()
    
    return customer_name_upper, customer_name_title, artist_name_upper, artist_name_title


def display_name_formats(customer_name, artist_name):
    """
    Display different string formatting options for educational purposes.
    
    Args:
        customer_name (str): The customer's name
        artist_name (str): The artist/band name
    """
    # Get formatted versions of the names
    customer_upper, customer_title, artist_upper, artist_title = format_name_display(customer_name, artist_name)
    
    # Display formatting examples
    print("\n" + "-"*60)
    print("STRING FORMATTING EXAMPLES")
    print("-"*60)
    print(f"   Customer Name (UPPERCASE): {customer_upper}")
    print(f"   Customer Name (Title Case): {customer_title}")
    print(f"   Artist Name (UPPERCASE): {artist_upper}")
    print(f"   Artist Name (Title Case): {artist_title}")
    print("-"*60)


def main():
    """
    Main function to orchestrate the concert ticket booking program.
    """
    # Display welcome message
    print("\n" + "*"*60)
    print("WELCOME TO THE CONCERT TICKET BOOKER")
    print("*"*60)
    print("Your digital ticket counter for all live events!")
    
    # Get booking details from user with validation
    while True:
        # Collect user input
        customer_name, artist_name = get_booking_details()
        
        # Validate the input
        if validate_booking_details(customer_name, artist_name):
            break
    
    # Display the booking confirmation
    display_booking_confirmation(customer_name, artist_name)
    
    # Display additional information (optional educational content)
    display_name_formats(customer_name, artist_name)
    display_booking_summary(customer_name, artist_name)
    
    # Final message
    print("\nEnjoy the show!")


# Entry point of the program
if __name__ == "__main__":
    main()
