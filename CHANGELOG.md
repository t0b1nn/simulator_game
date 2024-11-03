# Changelog

## [v0.3.1] - 03-11-2024

### Fixes
- **Signing up**: If no other accounts are available or saved, you can no longer log in.
---
## [v0.3.0] - 02-11-2024

### Added
- **New User class**: Introduced new User class replacing the old dictionary.
- **Deposit/Withdraw**: Updated these commands using User class.

### Fixes
- **Login.py rearrangement**: Quick rearrangement to login.py for readability
- **Bug fixes**: Minor bug fixes and performance improvements.

---
## [v0.2.4] - 02-11-2024

### Fixes
- **Improved readibility**: Enhanced variable names and data structures for better readability and maintainability.
- **Job application logic**: Refined the job application and work logic, making it easier to manage in the long run.

---
## [v0.2.3] - 02-11-2024

### Added
- **Blackjack XP**: Earns XP for playing blackjack.

### Fixes
- **Cancel option**: Fixed bug where "Invalid option" would randomly get printed.
- **Other minor bug fixes**: Quick variable rearrangement, etc.

---
## [v0.2.2] - 01-11-2024

### Added
- **Cancel option**: Option to cancel logging in/signing up.
### Fixes
- **Log in/Sign up logic**: Created new file to handle logging in.

---
## [v0.2.1] - 01-11-2024

### Fixes
- **Bank rob bugfix**: Fixed bug where player would always get bank robbed.
- **Improved prompts**: Kept input promps consistent.
- **Improved readibility***: Variable names changed.

---
## [v0.2.0] - 31-10-2024

### Added
- **Random events during sleep**: Random events can now occur when the player sleeps:
    - **Bank roberry**: A very low chance that a high portion of the user's bank money gets stolen.
    - **Pickpoket**: A relatively low chance that the user's whole wallet gets stolen.

### Fixes
- **Improved readability**: Variable names and iterable names changed for easier understanding and maintenance.
- **Work command cleanup**: Refined logic and structure of work and work_apply commands.

---
## [v0.1.0] - 31-10-2024
### Added
- Initial release of The $imulator with basic life simulation features.
- Command input system for user interaction.
