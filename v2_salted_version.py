import hashlib
import random

#login simulator
#able to register users, login, list users, quit

#<---functions--->

#encode / return hexidigest
def hash_password(password):
    encoded_password = password.encode()
    sha256 = hashlib.sha256()
    sha256.update(encoded_password)
    hashed_password = sha256.hexdigest()
    return hashed_password

#enter credentials and update user dict
def register_user(users):
    user_name = input('\nEnter new user name: ')
    user_password = input('\nEnter password for new user: ')
    salt = random.randint(0000,9999)
    combined_with_salt = (user_password + str(salt))
    hashed_password = hash_password(combined_with_salt)
    if user_name in users:
        print('\n----- USER ALREADY EXISTS ----- ')
        return 
    else:
        users[user_name] = (salt, hashed_password)
        print('\n----- USER REGISTERED SUCCESSFULY -----')
        return

#get input / hash / compare
def login_user(users):
    name = input('\nEnter login user name: ')
    password = input('\nEnter password: ')
    if name in users:
        salt, stored_hash = users[name]
        hashed_password = hash_password(password + str(salt)) 
        if hashed_password == stored_hash:
            print('\n----- LOGIN SUCCESSFUL -----')
            return
        else:   
            print('\n----- INVALID NAME AND OR PASSWORD -----')
            return
    else: 
        print('\n----- USER DOES NOT EXIST -----')
        return

#lists keys in users dict
def list_users(users):
    print('\n', users.keys())
    return

#lists options interface options
def list_options():
    print('\n1. Register User')
    print('\n2. Login')
    print('\n3. Exit')
    print('\n4. List Users')
    print('\n5. Crack Password')
    return

#get input from user 
def get_choice():    
    try:
        list_options()
        choice = input('\nMake a selection: ')
        choice = int(choice)
        return choice
    except ValueError:
        print('\nInvalid selection... Try again')
        return get_choice()

def crack_password(hash_to_crack):
    possible_passwords = ['123456', 'password', 'admin', 'qwerty']
    for password in possible_passwords:
        hashed_password = hash_password(password)
        if hashed_password == hash_to_crack:
            print('\nPassword: ' + password + ' ')
            return True
    print('\n----- PASSWORD NOT FOUND -----')

#run the interface, list options wait for input
def run_interface(users): 
    while True:
        choice = get_choice()   
        if choice == 1:
            register_user(users)
        elif choice == 2:
            print('\n----- LOG IN -----')
            login_user(users)
        elif choice == 3:
            print('\nGoodbye\n')
            break
        elif choice == 4:
            list_users(users)
        elif choice == 5:
            for key, value in users.items():
                if crack_password(value[1]):
                    print('\nUsername: ' + key)
                    print('\nPassword Hash: ' + value[1])
        else:
            print('\n----- INCORRECT INPUT TRY AGAIN -----')
            choice = get_choice()

users = {}
run_interface(users)


