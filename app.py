class Car:

    allObjects = []
    speed = 0

    def __init__(self, model, year, make):
        self.model = model
        self.year = year
        self.make = make
        self.speed = self.calculating_speed()

        self.allObjects.append(self)

    def accelerating(self):
        self.calculating_speed()

    def breaking(self):
        pass

    def hooting():
        pass

    def reversing():
        return "I am reversing"
  

    @classmethod
    def calculating_speed(cls):
        # The logic to calculate speed comes here
        return 180
    

peugeot = Car("308", 2018, "Peugeot")
prado = Car("TXL", 2020, "Prado")
merdes = Car("X50", 2021, "Mercedes")

print(peugeot.make)

print(prado.reversing())


for car in Car.allObjects:
    print(car.make)



