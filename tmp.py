# import random
#
#
# def get_user_input(prompt):
#     while True:
#         user_input = input(prompt)
#         if user_input.isnumeric():
#             return int(user_input)
#         elif user_input.lower() == 'x':
#             return 'x'
#         else:
#             print(f"{user_input} is not a number. Enter number: ")
#
#
# def play_game():
#     x = random.randint(1, 100)
#     print(x)
#     count = 0
#     while True:
#         user_number = get_user_input('Guess a number from 1 to 100. Enter number ("x" - for exit): ')
#         if user_number == 'x':
#             break
#         count += 1
#         if user_number == x:
#             print(f"You win!!! in {count} attempt(s)")
#             break
#         elif user_number > x:
#             print('Less. Try again ("x" - for exit): ')
#         else:
#             print('More. Try again ("x" - for exit): ')
#
#
# user_number = ' '
# while user_number != "y" and user_number != "n":
#     user_number = input('Start a new game? "y" - YES, "n" - NO: ').lower()
#     if user_number == "n":
#         break
#     elif user_number == "y":
#         play_game()


