'''
Lambda function: It's just an anymous function. A function wihtout a name and therefore can not be invoked. 
it executed on the fly(immediately)

Object Relationships:
1. Inheritiance
2. Associaton
3. Aggregation
4. Composition
5. Dependency
'''

#Inheritance relationship
class Animal:
    def speak(self):
        print("Animal speaks")


class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")


animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()





    