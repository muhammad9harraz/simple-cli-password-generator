import random
import string

def generate_password(length=12):

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

while True:
    print('\n-----Password Generator-----')
    try:
        length = int(input("\nEnter password length (min 6, max 50): "))
        if length < 6 or length > 50:
            print("\nInvalid length! Please choose between 6 and 50.")
            continue
    except ValueError:
        print("\nInvalid input! Please enter a number.")
        continue

    print("\nGenerated password:", generate_password(length))

    while True:
        again = input("\nGenerate another? [Y/N]: ").strip().lower()
        if again in ['y', 'n']:
            break
        print("\nInvalid input! Please enter Y or N.")

    if again == 'n':
        print("\nExiting Password Generator...")
        break