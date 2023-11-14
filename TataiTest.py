#coding: shift-jis

class Animal:
    def eat(self):
        print('動物は物を食べる')

class Dog(Animal):
    def eat(self):
        print('犬は骨を食べる')

class Cat(Animal):
    def eat(self):
        print('猫は魚を食べる')

class Person:
    def eat(self):
        print('人は何も食べる')

def fun(Obj):
    Obj.eat()

fun(Cat())
fun(Dog())
fun(Animal())
fun(Person())