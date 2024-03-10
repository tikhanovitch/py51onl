# import os
#
# print(os.getcwd()) # возвращает текущую диреторию
# print(os.path.exists("test_dir")) # проверяет наличие указаной директории
# # print(os.mkdir('test_dir_1')) # создает директорию
# open() - по умолчанию открывает файл для чтения 'r', если файл не найден - исключение
#                                      для записи 'w', если файл не найден - он создается, если найден - содержимое будет стерто
#                        для дозаписи в его конец 'a', если файл не найден - он создается, если найден - данные записываются в его конец
# close() - закрывает файл

# file = open("test_file.txt", "w")
# file.write("hello word")
# file.close()

# with open('test_file.txt', "r") as file:
# file = open("test_file.txt", "w")
# file.write("hello word")
# file.close()
# with open("test_file.txt", "w") as file:  - with - закрывает файл сама
#     for i in range(1, 10):
#         file.write(f'string number {i}' "\n")

# with open('test_file.txt', "r") as file:
#     file_data = (file.read())
#     print(repr(file_data))

    # file_data = file.read().rstrip().split("\n") - считывает все
    # file_data = file.readline() - считывает одну строку
    # file_data = file.readlines() - считывает все строки
    # print(repr(file_data))

    # students = {}
    # for line in file:
    #     student, mark = line.rstrip().split()
    #     students[student] = int(mark)
    # print(students)

import os
import json

# some_list = ["Mark", "Peter", "Kate"]
# some_serialization_string = json.dumps(some_list)
# print(some_serialization_string)
# some_loads_list = json.loads(some_serialization_string)
# print(some_loads_list)
#
# students = {
#     "Mark": 4,
#     "Nick": 9,
#     "Ann": 7,
#     "Peter": 4,
#     "Kate": 6
# }
# with open("students.json", "w") as file:
#     json.dump(students, file)
'''
Task 9
--------------------------1--------------------------
1.	Имеется текстовый файл. Получить текст, в котором в конце каждой строки из заданного
файла есть восклицательный знак.
info.txt

РЕШЕНИЕ:
with open('info.txt', "r") as file:
    file_data = ''
    for line in file:
        tmp_str = line.rstrip()
        if tmp_str[-1] == '!':
            file_data += tmp_str + '\n'
    print(file_data)

--------------------------2--------------------------
2.	Создать файл input.txt и записать в него 10 чисел через пробел. 
Считать из него эти числа. 
Затем записать их произведение в файл output.txt.

РЕШЕНИЕ:
with open('input.txt', 'w') as file:
    file.write('1 2 3 4 5 6 7 8 9 10')
with open('input.txt', 'r') as file:
    tmp_str = (file.read())
with open('output.txt', 'w') as file:
    numbers = [int(num) for num in tmp_str.split(' ')]
    product = 1
    for num in numbers:
        product *= num
    file.write(str(product))

--------------------------3--------------------------
3.	Список товаров, имеющихся на складе, включает в себя наименование 
товара, количество единиц товара, цену единицы. 
Вывести список товаров стоимость которых превышает 1 000 000 р.

РЕШЕНИЕ:
cost_more_mil = []
with open('goods.txt', 'r') as file:
    for line in file:
        line = line.rstrip()
        goods_info = line.split()
        print(goods_info)
        name, quantity, price = goods_info
        total_price = int(quantity) * int(price)
        if total_price > 1000000:
            cost_more_mil.append((name))
print('list of goods that cost more than a million', cost_more_mil)

--------------------------4--------------------------
4.	Написать программу “Викторина”. У вас есть 2 файла. В первом 
содержаться 10 вопросов (каждый вопрос в своей строке) во втором 
10 ответов( каждый ответ как и вопрос в своей строке). Вам нужно 
считывать по 1 вопросу из файла с вопросами и давать на них ответ. 
Если ответ верный, добавлять к счётчику верных ответов 1 балл. 
В конце программа выводит количество верных ответов на вопросы.

РЕШЕНИЕ:
with (open('questions.txt', 'r', encoding='utf-8') as q_file,
      open('answers.txt', 'r', encoding='utf-8') as a_file):
    correct_answers = 0
    while True:
        question = q_file.readline()
        answer = a_file.readline()
        if not question or not answer:
            break
        question = question.rstrip()
        answer = answer.rstrip()
        user_answer = input(question + " ")
        if user_answer == answer:
            print("Right!")
            correct_answers += 1
        else:
            print("Wrong.")
print("Correct answers:", correct_answers)

--------------------------5--------------------------
5.	Создать словарь в качестве ключа которого будет 5-ти значное 
число, а в качестве значений кортеж состоящий из 2-ух элементов – 
имя(str) и возраста(int). Сделать 5-6 элементов словаря и записать 
данный словарь на диск в файл json формата

РЕШЕНИЕ:
import json
some_dict = {
    12345: ('Pol', 47),
    23456: ('Jane', 25),
    34567: ('Peter', 27),
    45678: ('John', 31),
    56789: ('Rodger', 30),
    67890: ('Dmitry', 45)
}
print(some_dict)

with open('data.json', 'w') as json_file:
    json.dump(some_dict, json_file)

--------------------------6--------------------------
6.	Прочитать сохранённый json – файл и записать данные на диск в csv 
файл. Первое значение каждой строки должно начинаться со слова person, 
значения разделить ;

РЕШЕНИЕ:
import json
import csv

with open('data.json', 'r') as json_file:
    json_data = (json.load(json_file))
    print(type(json_data), json_data)
with open('data.csv', 'w') as csv_file:
    file_writer = csv.writer(csv_file, delimiter=';')
    file_writer.writerow(['person', 'name', 'age'])
__________
'''













