import hashlib

# --------------------------------------------------
# Version 1: Basic Password System (NO SALT)
# Demonstrates vulnerability to dictionary attacks
# --------------------------------------------------

# hash password using SHA-256
def hash_password(password):
    encoded = password.encode()
    sha256 = hashlib.sha256()
    sha256.update(encoded)
    return sha256.hexdigest()

# register user (stores hashed password ONLY)
def register_user(users):
    username = input('\nEnter new user name: ')
    password = input('Enter password for new user: ')

    if username in users:
        print('\n----- USER ALREADY EXISTS -----')
        return

    hashed = hash_password(password)
    users[username] = hashed

    print('\n----- USER REGISTERED SUCCESSFULLY -----')

# login user (compare hash of input)
def login_user(users):
    username = input('\nEnter login user name: ')
    password = input('Enter password: ')

    if username not in users:
        print('\n----- USER DOES NOT EXIST -----')
        return

    hashed_input = hash_password(password)

    if hashed_input == users[username]:
        print('\n----- LOGIN SUCCESSFUL -----')
    else:
        print('\n----- INVALID NAME OR PASSWORD -----')

# list users
def list_users(users):
    print('\nUsers:', users.keys())

# dictionary attack (WORKS in this version)
def crack_password(hash_to_crack):
    common_passwords = ['123456', 'password', 'admin', 'qwerty']

    for pwd in common_passwords:
        if hash_password(pwd) == hash_to_crack:
            print('\nPassword FOUND:', pwd)
            return True

    print('\n----- PASSWORD NOT FOUND -----')
    return False

# menu options
def show_menu():
    print('\n1. Register User')
    print('2. Login')
    print('3. Exit')
    print('4. List Users')
    print('5. Crack Password')

# get user choice
def get_choice():
    try:
        show_menu()
        return int(input('\nMake a selection: '))
    except ValueError:
        print('\nInvalid input. Try again.')
        return get_choice()

# main interface loop
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
            print('\n----- RUNNING DICTIONARY ATTACK -----')
            for user, stored_hash in users.items():
                if crack_password(stored_hash):
                    print('Username:', user)

        else:
            print('\n----- INVALID OPTION -----')

# run program
users = {}
run_interface(users)