"""
Secure Password Hint Tool
A program that shows a secure hint for password recovery.
"""

def main():
    """
    Main function to run the password hint tool.
    """
    # Step 1: Ask user for their password
    password = input("Enter your secret password: ")
    
    # Step 2: Strip accidental spaces
    cleaned_password = password.strip()
    
    # Step 3: Get first and last letters using string indexing
    first_letter = cleaned_password[0]
    last_letter = cleaned_password[-1]
    
    # Step 4: Print hint with uppercase letters
    print(f"Your password hint: It starts with {first_letter.upper()} and ends with {last_letter.upper()}")


# Entry point of the program
if __name__ == "__main__":
    main()
