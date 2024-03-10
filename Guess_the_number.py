import random

user_number = ' '
while user_number != "y" and user_number != "n":
    user_number = input('Start a new game? "y" - YES, "n" - NO: ')
    if user_number == "n":
        break
    if user_number == "y":
        while True:
            x = random.randint(1, 100)
            user_number = input('Guess a number from 1 to 100. Enter number ("x" - for exit): ')
            if user_number == 'x':
                break
            while not user_number.isnumeric():
                user_number = input(f"{user_number} is not number. Enter number: ")
            user_number = int(user_number)
            count = 0
            while user_number != x:
                if user_number > x:
                    user_number = input('Less. Try again ("x" - for exit): ')
                    if user_number == 'x':
                        break
                    while not user_number.isnumeric():
                        user_number = input(f"{user_number} is not number. Enter number: ")
                    user_number = int(user_number)
                    count += 1
                else:
                    user_number = input('More. Try again ("x" - for exit): ')
                    if user_number == 'x':
                        break
                    while not user_number.isnumeric():
                        user_number = input(f"{user_number} is not number. Enter number: ")
                    user_number = int(user_number)
                    count += 1
            if user_number == 'x':
                break
            count += 1
            print(f"You won!!! In {count} tries", end='\n')
            break
