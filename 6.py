'''
Task 6
--------------------------1--------------------------
1.	Напишите функцию minimum(a, b, c) - > int, вычисляющую минимум трёх чисел.
Функцию min() не использовать!

РЕШЕНИЕ:
def minimum(a: int, b: int, c: int) -> int:
"""
    Finds the minimum of three numbers.

    a: First number.
    b: Second number.
    c: Third number.
    return: Minimum of three numbers.
"""
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c

--------------------------2--------------------------
2.	Найдите минимальное 9 чисел с помощью функции написанной в предыдущей  задаче.
Новую функцию не создавать! Использовать функцию из предыдущей задачи!

РЕШЕНИЕ:
def minimum(a: int, b: int, c: int) -> int:
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c
numbers = list((map(int, input("input 9 numbers: ").split())))
temp_numb_1 = minimum(
    a=numbers[0],
    b=numbers[1],
    c=numbers[2]
)
temp_numb_2 = minimum(
    a=numbers[3],
    b=numbers[4],
    c=numbers[5]
)
temp_numb_3 = minimum(
    a=numbers[6],
    b=numbers[7],
    c=numbers[8]
)
min_numb = minimum(
    a=temp_numb_1,
    b=temp_numb_2,
    c=temp_numb_3
)
print(min_numb)

--------------------------3--------------------------
3.	Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию
distance(x1, y1, x2, y2), вычисляющую расстояние между точкой (x1, y1) и (x2, y2).
Считайте четыре действительных числа и выведите результат работы этой функции.

РЕШЕНИЕ:
import math

def distance(x1, y1, x2, y2) -> float:
# Distance
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Iiput coordinates
x1 = float(input("input x1: "))
y1 = float(input("input y1: "))
x2 = float(input("input x2: "))
y2 = float(input("input y2: "))


dist = distance(x1, y1, x2, y2)
print("Distance between points:", dist)


--------------------------4--------------------------
4.	Дано натуральное число n > 1. Проверьте, является ли оно простым.
Простое число – такое, которое делится на себя и на 1. Единица не простое число!
Программа должна вывести слово True, если число простое и False, если число составное.

РЕШЕНИЕ:
def prime_number(number: int):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


numb = int(input("input natural number: "))
if numb <= 0:
    print(numb, "not natural number")
if numb == 1:
    print(numb, "not prime number")
else:
    print(prime_number(numb))

--------------------------5--------------------------
5.	Напишите функцию fib(n), которая по данному целому неотрицательному n возвращает
n-e число Фибоначчи. Ищем число Фиббоначи через цикл! Рекурсию не использовать!

РЕШЕНИЕ:
def fib(n: int) -> int:
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        first_number = 1
        second_number = 1
        i = 3
        while i <= n:
            first_number, second_number = second_number, first_number + second_number
            i += 1
    return second_number

--------------------------6--------------------------
6.	Напишите реализацию функции closest_mod_5(x), принимающую в качестве единственного
аргумента целое число x и возвращающую самое маленькое целое число y, такое что:

-y больше или равно x
-y делится нацело на 5

РЕШЕНИЕ:
def closest_mod_5(x: int):
    y = x
    while y >= 0:
        if y % 5 == 0:
            return y
        y += 1
    return


ВАРИАНТ:
def closest_mod_5(x: int) -> int:
    if x >= 5:
        y = x // 5 * 5
        return y

--------------------------7--------------------------
7.	Напишите функцию modify_list(some_lst: list), которая принимает на вход
список целых чисел, удаляет из него все нечётные значения, а чётные нацело
делит на два. Функция не должна ничего возвращать, требуется только изменение
переданного списка.

РЕШЕНИЕ:
def modify_list(some_lst: list):
    for i in range(len(some_lst) - 1, -1, -1):
        if some_lst[i] % 2 == 0:
            some_lst[i] = int(some_lst[i] / 2)
        else:
            del some_lst[i]

--------------------------8--------------------------
8.	В языке Python есть некоторые ограничения на имена переменных. Имена переменных
-могут состоять только из цифр, букв и знаков подчеркивания.
-не могут начинаться с цифры.
Программист вводит строки с именами переменных. Для каждой переменной нужно вывести
"Можно использовать", если ее имя корректно, или "Нельзя использовать", если это не так.
Определив все нужные переменные, программист заканчивает ввод строкой "Поработали, и хватит".
Для проверки каждой строки используйте функцию check_variable(v). Для простоты будем считать,
что программист использует только латинские буквы.
Не может содержать : ! @ # $ % ^ & * ()

РЕШЕНИЕ:
def check_variable(v: str) -> str:
    if v[0].isdigit():
        return "Нельзя использовать"
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', ':']
    for symbol in symbols:
        if symbol in v:
            return "Нельзя использовать"
    return "Можно использовать"

......
a = check_variable(v="temp_1")
print(a)


'''