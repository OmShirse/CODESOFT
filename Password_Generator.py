import random
import string

def get_password_length():
    # keep asking until they give us a valid number
    while True:
        try:
            length = int(input("How long should the password be? (minimum 4): "))
            if length < 4:
                print("Come on, that's too short! Needs to be at least 4 characters.")
                continue
            return length
        except:
            print("That's not a number! Try again.")

def choose_complexity():
    print("\nWhat kind of password do you want?")
    print("1 - Simple (just letters and numbers)")
    print("2 - Medium (letters, numbers, and basic symbols)")
    print("3 - Strong (everything including special characters)")
    
    choice = input("Pick one (1, 2, or 3): ")
    
    if choice == "1":
        return string.ascii_letters + string.digits
    elif choice == "2":
        return string.ascii_letters + string.digits + "!@#$%"
    elif choice == "3":
        return string.ascii_letters + string.digits + string.punctuation
    else:
        # if they mess up just give them medium
        print("Invalid choice, going with medium complexity")
        return string.ascii_letters + string.digits + "!@#$%"

def generate_password(length, chars):
    # this was the easy part after figuring out the character sets
    password = ""
    for i in range(length):
        password += random.choice(chars)
    return password

def main():
    print("=" * 40)
    print("    Password Generator")
    print("=" * 40)
    
    # get what they want
    length = get_password_length()
    chars = choose_complexity()
    
    # make the password
    password = generate_password(length, chars)
    
    # show it
    print("\nYour generated password is:")
    print("-" * 40)
    print(password)
    print("-" * 40)
    
    # ask if they want another one
    again = input("\nGenerate another password? (y/n): ")
    if again.lower() == 'y' or again.lower() == 'yes':
        print("\n")
        main()  # just call the function again
    else:
        print("Thanks for using the password generator!")

if __name__ == "__main__":
    main()
