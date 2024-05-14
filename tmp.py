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

#
# class Car:
#     def __init__(self, model: str):
#         self._model = model
#     def info_car(self):
#         print(f"This is car {self._model}")
#
# class Truck(Car):
#     def info_truck(self):
#         # super().info_car()
#         # self.info_car()
#         print("This is Truck method")
#
#
# truck = Truck(model="Volvo")
#
#
# truck.info_truck()
# truck.info_car()
# truck.
#
# class GetInfoRoomMixin:
#     def info_room(self, current_time):
#         return "some_room"
#
#
# class GetInfoRoomMixin:
#     def info_room(self, current_time):
#         return "some_room"
#
#
# class User:
#     pass
#
#
# class Student(User, GetInfoRoomMixin):
#     pass
#
#
# class Professor(User, GetInfoRoomMixin):
#     pass
#
# class User:
#     pass
#
#
# class Student(User, GetInfoRoomMixin):
#     pass
#
#
# class Professor(User, GetInfoRoomMixin):
#     pass

name = 'Bob'


if name == 'Bob' or 'Tom' or 'Mike':
    print('Yes')
else:
    print('No')

