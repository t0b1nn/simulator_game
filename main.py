# main.py
# v0.2.1

comds_dict = {
    'main': {
        'help': 'See how to use commands.',
        'deposit': 'Deposit money into your bank account.',
        'withdraw': 'Withdraw money from your bank account.',
        'profile': 'View your profile information.',
        'work_apply': 'Apply for a job.',
        'work': 'Work a shift.',
        'hunt': 'Go hunting for resources.',
        'casino': 'Test your luck on money at the casino!',
        # 'music': 'Open music settings.',
        'sleep': 'Sleep the night.',
        'exit': 'Save and quit.',
    },
    # 'music': {
    #     'help': 'See how to use commands.',
    #     'volume': 'Adjust music volume.',
    #     'pause/play': 'Pause or play the music.',
    # },
    'casino': {
        'balance': 'View your balance.',
        'blackjack': 'Play a game of blackjack and earn (or lose) money!',
        'help': 'See what to do.',
        'exit': 'Leave the casino.',
    },
}
comds = {}
for key in comds_dict.keys(): comds[key] = list(comds_dict[key].keys())

jobs = [
    {'name':'Cashier', 'xp_rqd':0, 'shifts_rqd':2, 'xp_per_shift':2, 'salary':50},
    {'name':'Waiter', 'xp_rqd':10, 'shifts_rqd':2, 'xp_per_shift':5, 'salary':75},
    {'name':'Receptionist', 'xp_rqd':25, 'shifts_rqd':3, 'xp_per_shift':10, 'salary':150},
]
timers = {
    'work':0.0,
    'sleep':0.0,
    'hunt': 0.0,
    'casino': 0.0, 
}
loot_tables = {
    'hunt': {'raw mutton', 'raw chicken', 'raw beef', 'raw porkchop', },
}
items = {
    'raw mutton': {'type': 'food', 'hunger': 1, 'cookable': True, },
    'raw chicken': {'type': 'food', 'hunger': 1, 'cookable': True, },
    'raw beef': {'type': 'food', 'hunger': 1, 'cookable': True, },
    'raw porkchop': {'type': 'food', 'hunger': 1, 'cookable': True, },
}
week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', ]


def find(item, options):
    if item in options: return item
    else: print('Command not found.')
    for thing in options:
        if thing in item and input(f'Did you mean {thing}? [Y/N]  ').lower() == 'y': return thing
        different = 0
        try:
            for i in range(len(thing)):
                if item[i] != thing[i]: different += 1
            if different <= 2 and input(f'Did you mean {thing}? [Y/N]  ').lower() == 'y': return thing
        except:
            pass

def help(category):
    for c in comds[category]: 
        print(f'\033[1m{c}\033[0m: {comds_dict[category][c]}')
def obtain(item, quantity = 1):
    try:
        user['inventory'][item] += quantity
    except KeyError:
        user['inventory'][item] = quantity

def separator(word='', length=40):
    if word:
        word_length = len(word) + 2
        if word_length >= length:
            print(word)
        else:
            dashes = length - word_length
            left = '-' * (dashes // 2)
            right = '-' * (dashes - len(left))
            print(f'{left} {word} {right}')
    else:
        print('-' * length)
        
def login():
    global username, user
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
    if saves and input('If you would like to sign up, type "SIGN UP".\nIf you would like to log in, press enter.  ').lower() != 'sign up': # logs in with existing account
        user_found = False
        while not user_found:
            username = input('Please enter your username:  ')
            user_found = True if username in saves else print('User not found.')
        user.update(saves[username])
        password_wrong = True
        while password_wrong:
            password = maskpass.askpass('Please enter your password:    ')
            if password == b64_utils.decode(user['password']):
                password_wrong = False
            else:
                print('Incorrect password. Please try again.')
        print('Successfully logged in!\n')
        user['day'] -= 1
    else: # signs up with new account 
        confirmed = False
        while not confirmed:
            username = input('Type "CANCEL" to cancel.\nCreate a username:  ')
            if username not in saves.keys():
                if input(f'Enter "y" to confirm username {username}:  ').lower() == 'y': confirmed = True
            else:
                print('Username taken. Please create a new username.')
        password_confirmed = False
        while not password_confirmed:
            password = maskpass.askpass('Create a password:    ')
            password_confirmation = maskpass.askpass('Confirm password:    ')
            if password != password_confirmation:
                print('Passwords do not match.')
            else:
                password_confirmed = True
        user['password'] = b64_utils.encode(password)
        print('Account created!\n')

def game_loop():
    comd = 'sleep'
    while comd != 'exit':
        if comd == 'help': help('main')
        
        if comd == 'deposit':
            while True:
                try:
                    amount = float(input('How much cash would you like to deposit?  '))
                    if amount > user['wallet']:
                        print(f'You only have ${user["wallet"]} in your wallet!')
                    elif user['bank'] + amount > user['bank_cap']:
                        print(f'Your bank capacity is only ${user["bank_cap"]}!')
                    else:
                        break
                except ValueError:
                    print('Please enter a valid amount.')
            user['wallet'] -= amount
            user['bank'] += amount
            print(f"Successfully deposited ${amount}.")
        
        if comd == 'withdraw':
            while True:
                try:
                    amount = float(input('How much cash would you like to withdraw?  '))
                    if amount > user['bank']:
                        print(f'You only have ${user["bank"]} in your bank!')
                    else:
                        break
                except ValueError:
                    print('Please enter a valid amount.')
            user['bank'] -= amount
            user['wallet'] += amount
            print(f"Successfully withdrawn ${amount}.")
        
        if comd == 'profile':
            print(f'\n\033[1mProfile - {username}\033[0m')
            print(f'XP: {user["xp"]}\n')
            print(f'\033[1mStats\033[0m')
            print(f'Health: {user["health"]}/20')
            print(f'Hunger: {user["hunger"]}/20\n')
            print(f'\033[1mFinances\033[0m')
            print(f'Wallet: ${user["wallet"]}')
            print(f'Bank: ${user["bank"]}/{user["bank_cap"]}\n')
            print(f'\033[1mOccupation\033[0m')
            print(f'{"Job: " + user["job"]["name"] if user["job"] != {} else "Currently Unemployed"}')
            print(f'{"Weekly Shifts: " + str(user["weekly"]["work"]) + "/" + str(user["job"]["shifts_rqd"]) if user["job"] != {} else ""}\n')
        
        if comd == 'work_apply':
            print('Job List:\n')
            for j in jobs:
                print(f'\033[1m{j["name"]}\033[0m')
                print(f'Salary: {j["salary"]}')
                print(f'Weekly Shifts Required: {j["shifts_rqd"]}')
                print(f'XP Required: {j["xp_rqd"]}')
                print(f'XP Per Shift: {j["xp_per_shift"]}\n')
            applied = input('Choose a job:  ').lower()
            found = False
            for job in jobs:
                if job['name'].lower() == applied:
                    found = True
                    applied = job
                    break
            if not found:
                print('Job not found.')
                continue
            if applied['xp_rqd'] > user['xp']:
                print(f'You only have {user["xp"]} xp!')
                applied = ''
            elif random.randint(1, 4) == 1:
                applied = ''
                print("You failed the interview and didn't get the job.")
            else:
                user['job'] = applied['name']
                print(f'You nailed the interview and got the job as a {applied["name"].lower()}!')
        
        if comd == 'work':
            if not user['job']:
                print("You don't have a job to work at!")
            else:
                if time.time() - timers['work'] < 7:
                    print(f'You have already worked recently, try again in {round(7 - (time.time() - timers["work"]), 1)}s.')
                else:  
                    if user['daily']['work'] >= 2:
                        print('You have already worked twice today. Try again after sleeping.')
                    else:
                        word_list = ['bottle', 'house', 'pin', 'little', 'begin', 'running', 'base', 'colour', 'safely', 'eye', 'tablet', 'dance', 'forever', 'know', 'have', 'order', 'tiger', ]
                        colour_list = ['🔴', '🟠', '🟡', '🟢', '🔵', '🟣', '⚫️', '⚪️', '🟤']
                        orders = ['first', 'second', 'third', 'fourth', 'fifth',]
                        challenge = random.choice(['matching', 'order', 'highlow',])
                        correct = False
                        if challenge == 'matching':
                            words = random.sample(word_list, 3)
                            colours = random.sample(colour_list, 3)
                            print('Memorize words and colours!')
                            for i in range(3): print(f'{colours[i]} {words[i]}')
                            time.sleep(3)
                            for _ in range(3):
                                sys.stdout.write('\033[F')
                                sys.stdout.write('\033[K')
                                sys.stdout.flush()
                            index = random.choice(range(3))
                            if input(f'What word was next to {colours[index]}?  ').lower() == words[index]:
                                print('Correct!')
                                correct = True
                            else:
                                print(f'Wrong, the answer was {words[index]}.')
                        if challenge == 'order':
                            words = random.sample(word_list, 5)
                            print('Memorize words in order!')
                            for word in words: print(word)
                            time.sleep(3)
                            for _ in range(5):
                                sys.stdout.write('\033[F')
                                sys.stdout.write('\033[K')
                                sys.stdout.flush()
                            index = random.choice(range(5))
                            if input(f'What word was {orders[index]}?  ') == words[index]:
                                print('Correct!')
                                correct = True
                            else:
                                print(f'Wrong, the answer was {words[index]}.')
                        if challenge == 'highlow':
                            num = random.randint(1, 100)
                            guess = 0
                            guesses = 0
                            print('I am thinking of a number between 1 and 100.\nGuess the number in less than 8 tries!')
                            while guess != num:
                                guesses += 1
                                while True:
                                    try:
                                        guess = int(input('Guess my number:  '))
                                        break
                                    except:
                                        print('Please enter an integer.')
                                if num > guess:
                                    print('My number is higher.')
                                elif num < guess:
                                    print('My number is lower.')
                                else:
                                    print('Correct!')
                                    if guesses > 8:
                                        print(f'Good try, that took you {guesses} tries.')
                                    else:
                                        print(f'Good job! That only took you {guesses} tries!')
                                        correct = True
                        if correct:
                            user['wallet'] += jobs[user['job']]['salary']
                            user['xp'] += jobs[user['job']]['xp_per_shift']
                            print(f'Great work! You earned ${user["job"]["salary"]}.')
                        else:
                            user['wallet'] += jobs[user['job']]['salary'] / 2
                            user['xp'] += int(jobs[user['job']]['xp_per_shift'] / 2)
                            print(f'You earned ${jobs[user["job"]]["salary"] / 2}.')
                        timers['work'] = time.time()
                        user['daily']['work'] += 1
                        user['weekly']['work'] += 1
        
        if comd == 'hunt':
            if time.time() - timers['hunt'] < 10:
                print(f'You have already hunted recently, try again in {round(10 - (time.time() - timers["hunt"]), 1)}s.')
            else:
                loot = {}
                for i in loot_tables['hunt']:
                    loot[i] = random.randint(0, 2)
                if loot != {}:
                    print('You went hunting and got: ')
                    for i in loot:
                        if loot[i] != 0:
                            print(f'{loot[i]}x {i}')
                            obtain(i, loot[i])
                else:
                    print('You went hunting and returned empty-handed.')
                user['xp'] += 4
                timers['hunt'] = time.time()
        
        if comd == 'casino':
            if time.time() - timers['casino'] < 15:
                print(f'You have already gambled recently, try again in {round(15 - (time.time() - timers["casino"]), 1)}s.')
            elif user['wallet'] < 50:
                print('You need at least $50 to enter the casino.')
            else:
                separator('CASINO')
                while comd != 'exit':
                    comd = find(input('Enter a command:  ').lower(), comds['casino'])
                    if comd == 'balance':
                        print(f'Wallet: ${user["wallet"]}')
                    if comd == 'blackjack':
                        error = True
                        while error:
                            try:
                                bet = float(input('How much $ are you betting? (min $5)  '))
                                if bet <= 0:
                                    print('Enter a valid amount.')
                                elif bet < 5:
                                    print('Bet must be at least $5.')
                                elif bet > user['wallet']:
                                    print(f'You only have {user["wallet"]} in your wallet!')
                                else:
                                    error = False
                            except ValueError:
                                print('Enter a valid amount.')
                        game = blackjack.play()
                        if game == 'blackjack':
                            user['wallet'] += bet * 1.5
                            print(f'You earned ${bet * 1.5}!')
                        if game == 'win':
                            user['wallet'] += bet
                            print(f'You earned ${bet}.')
                        if game == 'push':
                            print(f'You get your ${bet} back.')
                        if game == 'loss':
                            user['wallet'] -= bet
                            print(f'You lost ${bet}.')
                    if comd == 'help': help('casino')
                    if user['wallet'] < 50:
                        print('You got kicked out because you have less than $50 in your wallet.')
                        comd = 'exit'
                separator()
                timers['casino'] = time.time()

        if comd == 'sleep':
            if time.time() - timers['sleep'] < 20:
                print(f'You have already slept recently, try again in {round(20 - (time.time() - timers["sleep"]), 1)}s.')
            else:
                # New day
                print()
                user['day'] += 1
                if user['day'] == 7:
                    user['day'] = 0
                    user['week'] += 1
                    if user['job'] != {}:
                        if user['weekly']['work'] < user['job']['shifts_rqd']:
                            user['job'] = {}
                            print('You got fired from your job.')
                    for i in list(user['weekly']):
                        user['weekly'][i] = 0
                for i in list(user['daily']):
                    user['daily'][i] = 0
                print(f'\033[1mWeek {user["week"]}, {week_days[user["day"]]}\033[0m')
                timers['sleep'] = time.time()
                if user['hunger'] > 0:
                    user['hunger'] -= 1
                else:
                    user['health'] -= 1
                if random.randint(1, 250) == 250:
                    user['bank'] *= round(user["bank"] * 0.25, 2)
                    print(f'${round(user["bank"] * 0.75, 2)} got stolen from your bank!')
                elif random.randint(1, 25) == 25:
                    user['wallet'] = 0
                    print('Your wallet got stolen!')
        
        if user['health'] <= 0:
            print('You died!')
            comd = 'exit'
        
        comd = find(input(f'Enter a command:  ').lower(), comds['main'])
        if not comd: continue


if __name__ == '__main__':
    import random, time, os, json, sys, maskpass, b64_utils
    from minigames import blackjack
    from pygame import mixer
    os.system('clear')
    mixer.init()
    mixer.music.load('lofi_mix.mp3')
    if input('Music? [Y/N]  ').lower() == 'y':mixer.music.play(-1)
    print('Welcome to The $imulator!')
    print('Type "help" for more information.\n')
    with open('saves.json', 'r') as file: saves = json.load(file)
    login()
    print('You wake up, ready for a new day...')
    game_loop()
    mixer.music.stop()
    saves[username] = user
    with open('saves.json', 'w') as file: json.dump(saves, file)
