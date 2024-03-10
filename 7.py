'''

Task 7
--------------------------1--------------------------
1.	Сгенерировать список нечётных двузначных  чисел.

РЕШЕНИЕ:
some_list = [i for i in range(11, 100, 2)]
print(some_list)

--------------------------2--------------------------
2.	Сгенерировать список из 10 чисел степени 2. От 1 до 10.

РЕШЕНИЕ:
some_list = [i**2 for i in range(1, 11)]
print(some_list)

--------------------------3--------------------------
3.	Сгенерировать список всех трёхзначных чисел кратных 5 и 3.

РЕШЕНИЕ:
some_list = [i for i in range(100, 1000) if i % 5 == 0 and i % 3 == 0]
print(some_list)

--------------------------4--------------------------
4.	Дан список, упорядоченный по не убыванию элементов в нем.
Определите, сколько в нем различных элементов. Set не использовать.

РЕШЕНИЕ:
some_lst = [1, 1, 1, 2, 3, 3, 3, 4, 4, 34, 34, 10, 100]
count = 0
last_element = None
for element in some_lst:
    if element != last_element:
        count += 1
        last_element = element
print(count)

--------------------------5--------------------------
5.	Напишите программу, на вход которой подаётся список чисел одной строкой.
Программа должна для каждого элемента этого списка вывести сумму двух его соседей.
Для элементов списка, являющихся крайними, одним из соседей считается элемент,
находящий на противоположном конце этого списка. Например, если на вход подаётся
список "1 3 5 6 10", то на выход ожидается список "13 6 9 15 7" (без кавычек).
Если на вход пришло только одно число, надо вывести его же. Вывод должен содержать
одну строку с числами нового списка, разделёнными пробелом.

Sample Input 1:
1 3 5 6 10
Sample Output 1:
13 6 9 15 7
Sample Input 2:
10
Sample Output 2:
10
Sample Input 3:
10 2
Sample Output 3:
4 20

РЕШЕНИЕ:
some_str = input('input numb list: ')
some_lst = [int(a) for a in some_str.split()]
if len(some_lst) == 1:
    print(some_str)
else:
    new_lst = [some_lst[i - 1] + some_lst[i + 1] for i in range(len(some_lst)) if i > 0 and i < len(some_lst) - 1]
    new_lst.insert(0, some_lst[-1] + some_lst[1])
    new_lst.append(some_lst[0] + some_lst[-2])
    new_str = ' '.join(map(str, new_lst))
    print(new_str)

--------------------------6--------------------------
6.	Создать список используя comprehension. Продублировать все неповторяющиеся элементы.

РЕШЕНИЕ:
some_lst = [i for i in range(1, 10)]
print(some_lst)

new_lst = []
for index in range(len(some_lst)):
    if index == len(some_lst) - 1 or some_lst[index] != some_lst[index + 1]:
        new_lst.append(some_lst[index])
        new_lst.append(some_lst[index])
else:
    pass
print(new_lst)

'''