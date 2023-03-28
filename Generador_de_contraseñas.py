import os
import random
import string

def random_password(password_type, length):
    if password_type == 1:
        chars = string.digits
    elif password_type == 2:
        chars = string.ascii_letters
    elif password_type == 3:
        chars = string.ascii_lowercase
    elif password_type == 4:
        chars = string.ascii_uppercase
    else:
        return print("Invalid password type")
    return ''.join(random.choice(chars) for i in range(length))

def menu():
    menu_options = {
        1: "Numeric password",
        2: "Alphabetic password",
        3: "Lowercase password",
        4: "Uppercase password",
    }
    print("\tPassword Generator\n")
    for option, description in menu_options.items():
        print(f"{option}: {description}")
    return menu_options

def save_passwords(passwords, password_type):
    try:    
        with open('./passwords.txt', 'w') as file:
            file.write("\tGenerated Passwords\n")
            for i, password in enumerate(passwords):
                file.write(f"{i+1}: {password_type[password[0]]}: {password[1]}\n")
    except:
        return False

if __name__ == "__main__":
    generated_passwords = []
    password_type = menu()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            menu()
            password_option = int(input("Password type (1-4): "))
            password_length = int(input("Password length: "))
            password = random_password(password_option, password_length)
            if password == "Invalid password type":
                print(password)
                continue
            generated_passwords.append((password_option, password))
            print(f"Your new password is: {password}")
        except ValueError:
            print("Please enter a valid number")
          
        another_password = input("Generate another password? (yes/no): ").lower()
        while another_password != "yes" and another_password != "no":
            another_password = input("Please enter 'yes' or 'no': ").lower()
        if another_password == "no":
            save_passwords(generated_passwords, password_type)
            print("Passwords saved to file")
            break