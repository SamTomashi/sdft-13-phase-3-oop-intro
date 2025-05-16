'''
It's one of the OOP principles that allows objects of idfferent 
classes to be treated as if they are of the same class through a common interface.
To make the code more flexible and reusable.


Two Main types: 
1. Duck Typing(Dynamic Typing)
2. Method Overriding (Runtime Polymorphism)
'''

#Dynamic Typing Polymorphism
# class Dog:
#     def speak(self):
#         return "woof!"

# class Cat:
#     def speak(self):
#         return "meow!"

# def animal_sound(animal):
#     print(animal.speak())

# dog = Dog()
# cat = Cat()

# animal_sound(dog)

#Method Overriding (Runtime Polymorphism)

# from abc import ABC, abstractmethod


class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"
    
class Snake(Animal):
    def speak(self):
        return "hiss!"
    
def make_sound(animal: Animal):
    print(animal.speak())


animals = [Snake(), Dog(), Cat()]

for animal in animals:
    make_sound(animal)