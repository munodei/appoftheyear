"""
Username and Message Formatter
A program that applies string transformations to create a formatted user profile.
"""

def main():
    """
    Main function to run the username and message formatter.
    """
    # Collect user input
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    bio_message = input("Enter a short bio about yourself: ")
    
    # Create username (first initial + last name in lowercase)
    username = (first_name[0] + last_name).lower()
    
    # Format full name in title case
    full_name = f"{first_name} {last_name}".title()
    
    # Process bio message
    stripped_bio = bio_message.strip()
    char_count = len(stripped_bio)
    modified_bio = stripped_bio.replace('I am', "I'm")
    
    # Display formatted output using f-strings
    print(f"\nUsername: @{username}")
    print(f"Full Name: {full_name}")
    print(f"Bio: {modified_bio}")
    print(f"Bio Character Count: {char_count}")


# Entry point of the program
if __name__ == "__main__":
    main()
