# login.py
# v0.3.1

import maskpass, b64_utils, json
with open('saves.json', 'r') as file: saves = json.load(file)

def signup_user():
    global user, username, saves, done
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
    confirmed = False
    while not confirmed:
        username = input('Create a username:  ')
        if username.lower() == 'cancel':
            if saves:
                print('Sign-up cancelled.')
            return
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
    global username, saves, done
    while not done:
        user_found = False
        while not user_found:
            username = input('Please enter your username:  ')
            if username.lower() == 'cancel':
                print('Log-in cancelled.')
                return
            user_found = True if username in saves else print('User not found.')
        user.update(saves[username])
        password_wrong, password_cancel = True,  False
        while password_wrong:
            password = maskpass.askpass('Please enter your password:    ')
            if password.lower() == 'cancel':
                password_cancel = True
                print('Password entry cancelled.')
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
    print('Type "CANCEL" to cancel action.')
    done = False
    while not done:
        if saves:
            choice = input('If you would like to sign up, type "SIGN UP"\nIf you would like to log in, type "LOG IN".  ').lower()
        else:
            choice = 'sign up'
        if choice == 'sign up':
            signup_user()
        elif choice == 'log in':
            login_user()
        else:
            print('Invalid action.')
    return user, username

if __name__ == '__main__': main()
