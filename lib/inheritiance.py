class Vehicule:
    allVehicule = []
    def __init__(self, type):
        self.type = type

        self.allVehicule.append(self)

    def move(self, movement):
        return f"{self.type} {movement}"
    
    def accelerating():
        pass
    

class Car(Vehicule):
    wheels = 4
    def __init__(self, model, year, make):
        self.model = model
        self.year = year
        self.make = make
        super().__init__(type="Car")


class Plane(Vehicule):
    pass

class Train(Vehicule):
    pass


class Motorbike(Vehicule):
    pass



toyota = Car('Prado', 2020, "Toyota")

print(toyota.type)

print(Vehicule.allVehicule)
