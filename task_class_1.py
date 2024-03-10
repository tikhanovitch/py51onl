'''
1.	Создать класс с двумя переменными. Добавить функцию вывода на экран и функцию изменения этих переменных.
Добавить функцию, которая находит сумму значений этих переменных, и функцию которая находит наибольшее значение
из этих двух переменных.

class Variables:

    def __init__(self, var1: int, var2: int) -> None:
        self.var1 = var1
        self.var2 = var2

    def info_var(self) -> None:
        print(f"Variable 1: {self.var1}, Variable 2: {self.var2}")

    def change_variables(self, new_var1: int, new_var2: int):
        self.var1 = new_var1
        self.var2 = new_var2

    def sum_variables(self):
        return self.var1 + self.var2

    def max_variable(self):
        return max(self.var1, self.var2)



# 2.	Описать класс, реализующий десятичный счетчик, который может увеличивать или уменьшать свое значение на единицу
# в заданном диапазоне. Предусмотреть инициализацию счетчика значениями по умолчанию и произвольными значениями.
# Счетчик имеет два метода: увеличения и уменьшения, — и свойство, позволяющее получить его текущее состояние.
# Написать программу, демонстрирующую все возможности класса.

class Decimal_Counter:
    MIN_VALUE = 0
    MAX_VALUE = 10

    def __init__(self, value=MIN_VALUE) -> None:
        self.value = value

    def increment(self):
        if self.value < self.MAX_VALUE:
            self.value += 1
        else:
            print("The counter has reached its maximum value")

    def decrement(self):
        if self.value > self.MIN_VALUE:
            self.value -= 1
        else:
            print("The counter has reached its minimum value")

    @property
    def current_value(self):
        return self.value

'''
