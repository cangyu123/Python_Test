class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def fun(self):
        print('Person Method!')

    def info(self):
        print(f'Name:{self.name},Age:{self.age}')

class Student(Person):
    def __init__(self,name,age,stu_id):
        super().__init__(name,age)
        self.stu_id = stu_id

    def info(self):
        super().info()
        print(f'StudentID:{self.stu_id}')

class Teacher(Person):
    def __init__(self,name,age,tea_id):
        super().__init__(name,age)
        self.tea_id = tea_id

    def info(self):
        super().info()
        print(f'TeacherID:{self.tea_id}')

stu1 = Student('LI',23,1001)
tea1 = Teacher('tanaka',45,10009)
per1 = Person('\\',23)

stu1.info()
tea1.info()
stu1.fun()

print(dir(stu1))