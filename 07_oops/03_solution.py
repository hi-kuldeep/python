class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    
    def full_name(self):
        return f"Brand: {self.brand}, Model: {self.model}"

class ElectricCar(Car):
    def __init__(self , brand , model , battery_size):
        super().__init__(brand , model)
        self.battery_size = battery_size

    def electric_car_name(self):
        return f"Brand: {self.brand}, Model: {self.model}, Battery Size: {self.battery_size}"
    

my_car = ElectricCar("Toyota", "Urban Cruiser" , "50kwh")

print(my_car.electric_car_name())
print(my_car.battery_size)
print(my_car.full_name())
    