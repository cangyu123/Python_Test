#coding: shift-jis

class Studenr:
    native = 'Hello World'

    def __init__(self,name,age,num):
        self.name = name
        self.__age = age #私用化、外部訪問は不可
        self.num = num

    def eat(self):
        print(self.name,'is eatting')

    def info(self):
        print('My name is',self.name,'age is',self.__age,'id is',self.num)

    classmethod
    def ClassMs():
        print('I am ClassMethod!')

    staticmethod
    def StaticMs():
        print('I am StaticMs')

stu1 = Studenr('Li',25,1001)

print(stu1.native)
stu1.eat()
stu1.info()
Studenr.ClassMs()
Studenr.StaticMs()
print(stu1._Studenr__age) #私用化の変数を強制アクセス