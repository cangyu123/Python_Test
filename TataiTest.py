#coding: shift-jis

class Animal:
    def eat(self):
        print('�����͕���H�ׂ�')

class Dog(Animal):
    def eat(self):
        print('���͍���H�ׂ�')

class Cat(Animal):
    def eat(self):
        print('�L�͋���H�ׂ�')

class Person:
    def eat(self):
        print('�l�͉����H�ׂ�')

def fun(Obj):
    Obj.eat()

fun(Cat())
fun(Dog())
fun(Animal())
fun(Person())