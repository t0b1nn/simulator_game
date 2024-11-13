
# The $imulator

**Version**: v0.4.0 and edit

A text-based simulation game where you can dive into the thrill of life’s adventures—manage your finances, try your luck at the casino, hunt for resources, develop skills, and much more!

## Features

- **Life Simulation**
- **Jobs**: Apply for jobs and get interviewed, work with various salaries, complete minigames to complete shifts.
- **Experience Points**: Earn XP from doing different things such as working or hunting, higher XP unlocks new jobs and more.
- **Casino Fun**: Visit the casino and test your luck on Blackjack and other games!
- **Hunting, Fishing, Digging**: Obtain items from hunting in various ways.
- **Save Files**: Save your progress with this basic password-protected save file system.
- **Basic Inventory**: Own various items.
- **Log in/Sign Up**
- **Day/Week Cycle**

## Installation

To install and run the game, you need to have **Pip**, **Python** and **Git** installed on your system.

### Install Requirements

- **Python**: Download from the official [Python website](https://www.python.org/downloads/).
- **Git**: Download from the official [Git website](https://git-scm.com/downloads).

1. Clone the repository:
```bash
git clone https://github.com/t0b1nn/simulator_game
```
2. Navigate to the project directory:
```bash
cd simulator_game
```
3. Install required dependencies:
- On Windows (Command Line/Powershell):
```bash
pip install pygame maskpass
```
- On Mac (Terminal):
```zsh
pip3 install pygame maskpass
```

## Usage

Run the main game script:
- On Windows (Command Line/Powershell):
```bash
python main.py
```
- On Mac (Terminal):
```zsh
python3 main.py
```
Type "help" on an "Enter a command" input for command help. Please sign up at the start when playing for the first time.

## Roadmap

- Add more functionality to XP, hunger and health.
- Create more jobs.
- Add more casino items.
- Add more flexibility for sign up/log in system.
- Create a battle system for more engagement.

## Contributing

Contributions are always welcome! If you would like to contribute, feel free to sumbit a pull request.

##  Links

- GitHub: [@t0b1nn](https://www.github.com/t0b1nn)
- Email: vadakkeltobin@gmail.com

## Directory Structure

```
simulator_game/
├── CHANGELOG.md
├── LICENSE
├── README.md
├── __pycache__/
│   ├── b64_utils.cpython-311.pyc
│   └── login.cpython-311.pyc
├── b64_utils.py                        # Utilities for Base 64 encryption
├── lofi_mix.mp3                        # Background music for game
├── login.py                            # Log in & Sign up feature
├── main.py                             # Main game file
├── minigames/
│   ├── __pycache__/
│   │   └── blackjack.cpython-311.pyc
│   └── blackjack.py                    # Blackjack game implementation
└── saves.json                          # User save files
```

## License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).
