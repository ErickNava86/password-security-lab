import bcrypt
import json

def hash_password(password):
    encoded_password = password.encode()
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(encoded_password, salt)
    return hashed_password


def login_user(users):
    username = input('\nEnter username: ')
    password = input('\nEnter Password: ')
    encoded_password = password.encode()

    if username not in users:
        print('\n-----THIS USER NAME DOES NOT EXIST-----.')
        return
    
    if users[username]["attempts"] >= 3:
        print("\n-----ACCOUNT LOCKED-----")
        return
    
    stored_hash = users[username]["password"]

    if bcrypt.checkpw(encoded_password, stored_hash):
        print('\n-----LOGIN SUCCESSFUL!-----')
        users[username]["attempts"] = 0
    else:
        print('\n-----INCORRECT PASSWORD----- ')
        
        users[username]["attempts"] += 1
        attempts_left = 3 - users[username]["attempts"]
        
        if users[username]["attempts"] >= 3:
            if attempts_left > 0:
                print("\n-----ACCOUNT LOCKED-----")
                print(f'\n-----YOU HAVE {attempts_left} TRIES LEFT-----')
                return

    

def register_user(users):
    name = input('\nEnter name: ')
    password = input('\nEnter new password: ')
    hashed_password = hash_password(password)
    
    if name in users:
        print('\n-----USER ALREADY EXISTS-----!')
        return
    
    users[name] = {
    "password": hashed_password, 
    "attempts": 0
    }
    
    #write to JSON file
    save_users(users)

    print("\n-----USER REGISTERED SUCCESSFULLY-----")


def get_menu_input(users):
    while True:
        print('\n1. Register')
        print('\n2. Login')
        print('\n3. Exit')
        
        try:
            user_input = int(input('\nEnter choice: '))
        except ValueError:
            print('\n-----Invalid Input. Enter a number-----')
            continue
        
        if user_input == 1:
            register_user(users)
        elif user_input == 2:
            login_user(users)
        elif user_input == 3:
            print('\n---Goodbye---')
            return
        else:
            print('\n-----INVALID CHOICE-----')

def save_users(users):
    safe_users = {}

    for user in users:
        #extract
        password_bytes = users[user]["password"]
        password_str = password_bytes.decode()

        attempts = users[user]["attempts"]

        #update users
        safe_users[user] = {
            "password": password_str,
            "attempts": attempts
        }

    #write to json file    
    with open("users.json", "w") as file:
        json.dump(safe_users, file)


    print('\n-----USER SAVED SUCCESSFULY-----')
    return
    

def load_users():
    #open readable file/ check if no file exist
    loaded_users = {}
    try:
        with open("users.json", "r") as file:
            data = json.load(file)


    except FileNotFoundError:
        return {}
    

    #extract info append to new hash loaded_users
    for user in data:
        password_str = data[user]['password']
        password_bytes = password_str.encode()
        
        attempts = data[user]["attempts"]

        loaded_users[user] = {
            "password": password_bytes,
            "attempts": attempts
        }
    
    print('\n-----USERS LOADED SUCCESSFULY---')
    return loaded_users

    def validate_password(password):
        #common password check 
        common_passwords = ["password", "123456", "admin", "qwerty"]
        if password in common_passwords:
            print('\n-----PASSWORD TOO COMMON-----')
            return False

        #length check
        if len(password) < 8:
            print('\n-----PASSWORD IS TOO SHORT. NEED AT LEAST 8 CHARACTERS-----')
            return False

        #checks for a number
        if not any(letter.isdigit() for letter in password):
            print('\n-----PASSWORD MUST HAVE A NUMBER-----')
            return False
        
        #checks for a capital letter
        if not any(letter.isupper() for letter in password):
            print('\n-----PASSWORD NEEDS A CAPITAL LETTER-----')
            return False
        
        #checks for lowercase letter
        if not any(letter.islower() for letter in password):
            print('\n-----PASSWORD NEEDS A LOWERCASEE LETTER-----')
            return False
        
        return True


users = load_users()
get_menu_input(users)















