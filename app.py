class Car:

    allObjects = []
    speed = 0

    country = "Kenya"

    def __init__(self, model, year, make):
        self.model = model
        self.year = year
        self.make = make
        self.speed = self.calculating_speed()

        self.allObjects.append(self)

    def accelerating(self):
        self.calculating_speed()

    def breaking(self):
        self.speed

    def hooting():
        pass

    @staticmethod
    def reversing():
        return "I am reversing"
  

    @classmethod
    def calculating_speed(cls):
        # The logic to calculate speed comes here
        return 180
    

peugeot = Car("208", 2020, "Peugeot")
mobius = Car("Model 3", 2022, "Mobius")

peugeot.country = "France"

print(peugeot.country)

print(mobius.country)

print(mobius.year)


'''
Principles of OOP:
1. Inheritance: Is the ability of a child class to inherit porperties and bhevaiouse of another class
2. Encapsulation: The ability to protect of our code/classs/object from external modification
3. Abstraction: The ability hide the complexity of our code/logic
4. Polymorphism: The ability of a class to have many forms
'''


