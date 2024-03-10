'''
Task 5
--------------------------1--------------------------
1.	Вывести на экран число "10" 20 раз столбиком.

РЕШЕНИЕ:
numb = "10"
for i in range(20):
    print(numb)

--------------------------2--------------------------
2.	Дано число N.
Составить программу выводящую кубы чисел от 1 до N в одну строку.

РЕШЕНИЕ:
numb = int(input("eneter number: "))
for i in range(1, numb + 1):
    print(i**3, end=" ")

--------------------------3--------------------------
3.	Выведите на экран в одну строку числа от 100 до
-100 включительно.

РЕШЕНИЕ:
for i in range(100, -101, -1):
    print(i)

--------------------------4--------------------------
4.	Необходимо вывести все четные числа на отрезке [a; a * 10]

РЕШЕНИЕ:
numb = int(input("input number: "))
for i in range(numb, numb * 10 + 1):
    if i % 2 == 0:
        print(i, end=" ")

--------------------------5--------------------------
5.	Найти сумму всех целых чисел от 100 до 500 включительно.

РЕШЕНИЕ:
summa = 0
for i in range(100, 501):
    summa += i
print(summa)

--------------------------6--------------------------
6.	Найти произведение всех целых чисел от 5 до 20 включительно.

РЕШЕНИЕ:
prod_of_num = 1
for i in range(5, 21):
    prod_of_num *= i
print(prod_of_num)

--------------------------7--------------------------
7.	Дано натуральное число n. Вывести на экран факториал этого числа.

РЕШЕНИЕ:
numb = int(input("input number: "))
factorial = 1
for i in range(1, numb + 1):
    factorial *= i
print(factorial)

--------------------------8--------------------------
8.	Дано число n. Посчитать сумму всех чётных чисел от 0 до n.

РЕШЕНИЕ:
numb = int(input("input number: "))
summ = 0
i = 0
while i <= numb:
    if i % 2 == 0:
        summ += i
        i += 1
    else:
        i += 1
print(summ)

--------------------------9--------------------------
9.	Дано натуральное число. Определить произведение цифр
в нем которые кратны 2, кроме числа 0.

РЕШЕНИЕ:
numb = int(input("input number: "))
numb_str = str(numb)
numb_of_digits = int(len(numb_str))
prod = 1
index = 0
while index < numb_of_digits:
    digit = int(numb_str[index])
    if digit % 2 == 0 and digit != 0:
        prod *= digit
        index += 1
    else:
        index += 1
print(prod)

--------------------------10--------------------------
10.	Дано число n. Вывести на экран числа 1, 4, 9, 16, 25, ... которые меньше n.

Sample Input :
15
Sample Output :
1 4 9

РЕШЕНИЕ:
numb = int(input("input number: "))
i = 1
while i < numb:
    if i ** 2 < numb:
        print(i ** 2)
        i += 1
    else:
        break

--------------------------11--------------------------
11.	Дано число n. Среди чисел 1, 4, 9, 16, 25, ... найти первое, которые больше n.
Sample Input :
5
Sample Output :
9

РЕШЕНИЕ:
numb = int(input("input number: "))
i = 1
while i < numb:
    if i ** 2 <= numb:
        i += 1
    else:
        print(i ** 2)
        break

--------------------------12--------------------------
12.	Дано число n. Определить первую цифру этого числа.

РЕШЕНИЕ:
numb = int(input("input number: "))
numb_str = str(numb)
print(int(numb_str[0]))

--------------------------13--------------------------
13.	Дано число n. Найти сумму цифр в этом числе.

РЕШЕНИЕ:
numb = int(input("input number: "))
numb_str = str(numb)
numb_of_digits = int(len(numb_str))
summ = 0
index = 0
while index < numb_of_digits:
    digit = int(numb_str[index])
    summ += digit
    index += 1
print(summ)

--------------------------14--------------------------
14.	Дано натуральное число n. Найти значение минимальной
цифры в данном числе

РЕШЕНИЕ:
numb = int(input("input number: "))
numb_str = str(numb)
numb_of_digits = int(len(numb_str))
min_digit = int(numb_str[0])
index = 1
while index < numb_of_digits:
    tmp_dig = int(numb_str[index])
    if min_digit < tmp_dig:
        index += 1
    else:
        min_digit = tmp_dig
        index += 1
print(min_digit)

--------------------------15--------------------------
15.	Дана строка. Преобразовать строку: после каждой буквы 'z'
добавить символ '!'.

some_str = input("input string: ")
new_str = ""
for elem in some_str:
    if elem != "z":
        new_str += elem
    else:
        new_str += "z!"
print(new_str)

--------------------------16--------------------------
16.	Вывести строку, удалив из нее повторные вхождения символов.

РЕШЕНИЕ:
some_str = input("input str: ")
tmp_str = ""
for i in range(len(some_str)):
    if some_str[i] not in tmp_str:
        tmp_str += some_str[i]
print(tmp_str)

--------------------------17--------------------------
17.	Удалить в строке все буквы 'b', непосредственно за которыми идет
цифра. Удалить из текста символы, являющиеся строчными латинскими буквами.

РЕШЕНИЕ:
some_str = input("input str: ")
tmp_str = ""
for i in range(len(some_str)):
    if some_str[i] == "b" and some_str[i + 1].isdigit():
        tmp_str += ""
    else:
        tmp_str += some_str[i]
print(tmp_str)
tmp_str_1 = ""
for i in range(len(some_str)):
    if some_str[i] not in "abcdefghigklmnopqrstuvwxyz":
        tmp_str_1 += some_str[i]
print(tmp_str_1)

'''