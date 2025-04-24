class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
class Car(Vehicle):
    def __init__(self,brand,model,num_doors):
        super().__init__(brand,model)
        self.num_doors=num_doors
class ElectricCar(Car):
    def __init__(self,brand,model,num_doors,battery_capacity):
        super().__init__(brand,model,num_doors)
        self.battery_capacity=battery_capacity

obj1=ElectricCar('BMW','z2',5,40)
print(obj1.brand,obj1.model,obj1.num_doors,obj1.battery_capacity)
