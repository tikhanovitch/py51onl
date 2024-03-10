class DatabaseConnection:
    pass

class Student:
    LEGS = 2  # атрибут класса (если переменная не меняется, то большими буквами)
  # age = 20 не верно, т.к. каждый студент имеет свой возраст
    def __init__(self,
                 name: str,
                 age: int,
                 average_mark: float
    )-> None:  # инициализатор класса self - ссылка на экземпляр
        self.name = name
        self.age = age
        self.average_mark = average_mark


    def __new__(cls, *args, **kwargs):
        print("new object created")
        return super(Student, cls).__new__(cls)


    def info_student(self):
        print(f"student => {self.name} {self.age} {self.average_mark}")


    def year_later(self):
        self.age += 1


    def __del__(self):
        print(f"delete {self}")


student_1 = Student(name="Jack", age=19, average_mark=7.2)  # создаем экзмепляр класса(объект класса Student)
student_2 = Student(name="John", age=18, average_mark=5.6)
print(student_1.name, student_2.name)
student_1.info_student()
student_2.info_student()

student_1.year_later()
student_2.year_later()

student_1.info_student()
student_2.info_student()

