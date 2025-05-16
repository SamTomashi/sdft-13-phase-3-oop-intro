'''
Composition:
An object relationships concept that enforces a strong ownership
whereby a parent class creates and controls the child
'''

class Engine:
    def __init__(self, power):
        self.power = power

    def ignite(self):
        print(f'Engine with {self.power} has ignited')



class Car:
    def __init__(self, model, engine_power):
        self.model = model
        self.engine = Engine(engine_power) #Composition

    def start(self):
        print(f"{self.model} is starting...")
        self.engine.ignite()

# engine1 = Engine(120)
# engine1.ignite()

car1 = Car("Toyota", 2500)
car1.start()


'''
 Association - Aggregation
 Composition - Inheritance
'''
