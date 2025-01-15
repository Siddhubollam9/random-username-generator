import random

# Pre-defined lists of adjectives and nouns
adjectives = ["Cool", "Happy", "Brave", "Lucky", "Bright", "Quick", "Clever", "Fierce"]
nouns = ["Tiger", "Dragon", "Phoenix", "Panda", "Eagle", "Wolf", "Fox", "Hawk"]
special_characters = ["!", "@", "#", "$", "%", "^", "&", "*"]

def generate_username_v2(include_numbers=True, include_special_characters=True):
    """
    Generate a random username by combining an adjective and a noun.
    Optionally append numbers and special characters.

    Args:
        include_numbers (bool): Include numbers in the username.
        include_special_characters (bool): Include special characters in the username.

    Returns:
        str: A randomly generated username.
    """
    username = random.choice(adjectives) + random.choice(nouns)
    if include_numbers:
        username += str(random.randint(0, 99))
    if include_special_characters:
        username += random.choice(special_characters)
    return username

def get_user_input(prompt, default=None, allowed_values=None):
    """
    Get and validate user input with optional defaults and constraints.

    Args:
        prompt (str): The message to display to the user.
        default (str): Default value if no input is provided.
        allowed_values (list): List of valid input values (optional).

    Returns:
        str: Validated user input.
    """
    while True:
        user_input = input(prompt).strip().lower()
        if not user_input and default is not None:
            return default
        if allowed_values and user_input not in allowed_values:
            print(f"Invalid input. Please choose from {', '.join(allowed_values)}.")
        else:
            return user_input

def generate_multiple_usernames():
    """
    Generate multiple usernames based on user preferences and optionally save them to a file.
    """
    print("Welcome to the Random Username Generator!")

    include_numbers = get_user_input("Include numbers? (yes/no, default: yes): ", default="yes", allowed_values=["yes", "no"]) == "yes"
    include_special_characters = get_user_input("Include special characters? (yes/no, default: no): ", default="no", allowed_values=["yes", "no"]) == "yes"

    while True:
        try:
            count = int(input("How many usernames would you like to generate? (default: 5): ") or 5)
            if count > 0:
                break
            print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    usernames = [generate_username_v2(include_numbers, include_special_characters) for _ in range(count)]

    print("\nGenerated Usernames:")
    for i, username in enumerate(usernames, start=1):
        print(f"{i}: {username}")

    save = get_user_input("\nSave these usernames to a file? (yes/no, default: no): ", default="no", allowed_values=["yes", "no"]) == "yes"
    if save:
        filename = input("Enter the filename (default: usernames.txt): ").strip() or "usernames.txt"
        try:
            with open(filename, "w") as file:
                for username in usernames:
                    file.write(username + "\n")
            print(f"Usernames saved to {filename}.")
        except Exception as e:
            print(f"Error saving to file: {e}")

if __name__ == "__main__":
    generate_multiple_usernames()
