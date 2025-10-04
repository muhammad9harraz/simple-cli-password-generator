# Password Generator CLI

A simple Python command-line tool to generate strong random passwords using letters, digits, and special characters.

## Features

- Generate secure random passwords of customizable length.
- Supports length between 6 and 50 characters.
- Input validation for invalid numbers and ranges.
- Easy option to generate multiple passwords without restarting the program.

### Example Usage

-----Password Generator-----
Enter password length (min 6, max 50): 10

Generated password: -r-mX^-~<s

Generate another? [Y/N]: y

-----Password Generator-----
Enter password length (min 6, max 50): 4

Invalid length! Please choose between 6 and 50.

-----Password Generator-----
Enter password length (min 6, max 50): 8

Generated password: QPoxQ6(y

Generate another? [Y/N]: j

Invalid input! Please enter Y or N.

Generate another? [Y/N]: n

Exiting Password Generator...