# login.py
# v0.2.2

import maskpass, b64_utils, json
with open('saves.json', 'r') as file: saves = json.load(file)

def signup_user():
    global done
    confirmed = False
    while not confirmed:
        username = input('Create a username:  ')
        if username.lower() == 'cancel': return
        if username not in saves.keys():
            if input(f'Enter "y" to confirm username {username}:  ').lower() == 'y': confirmed = True
        else:
            print('Username taken. Please create a new username.')
    password_confirmed = False
    while not password_confirmed:
        password = maskpass.askpass('Create a password:    ')
        if password.lower() == 'cancel':
            print('Password cannot be "cancel".')
            continue
        password_confirmation = maskpass.askpass('Confirm password:    ')
        if password != password_confirmation:
            print('Passwords do not match.')
        else:
            password_confirmed = True
    user['password'] = b64_utils.encode(password)
    done = True
    print('Account created!\n')

def login_user():
    global done
    while not done:
        user_found = False
        while not user_found:
            username = input('Please enter your username:  ')
            if username.lower() == 'cancel': return
            user_found = True if username in saves else print('User not found.')
        user.update(saves[username])
        password_wrong, password_cancel = True,  False
        while password_wrong:
            password = maskpass.askpass('Please enter your password:    ')
            if password.lower() == 'cancel':
                password_cancel = True
                break
            if password == b64_utils.decode(user['password']):
                password_wrong = False
            else:
                print('Incorrect password. Please try again.')
        if password_cancel: continue
        print('Successfully logged in!\n')
        done = True
        user['day'] -= 1

def main():
    global username, user, done
    user = {
        'health': 20,
        'hunger': 20,
        'wallet': 0.0,
        'bank': 0.0,
        'bank_cap': 500000.0,
        'job': {},
        'xp': 0,
        'inventory': {},
        'day': -1,
        'week': 1,
        'daily': {'work':0,},
        'weekly': {'work':0,},
    }
    done = False
    while not done:
        choice = input('If you would like to sign up, type "SIGN UP"\nIf you would like to log in, type "LOG IN".  ').lower()
        if choice == 'sign up':
            signup_user()
        if choice == 'log in':
            login_user()
        else:
            print('Invalid action.')

if __name__ == '__main__': main()
