class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model

    def get_brand_name(self):
        return f"Brand: {self.__brand}"

    def fuel_type(self , type):
        return type

class ElectricCar(Car):
    def __init__(self , brand , model , battery_size):
        super().__init__(brand , model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"
    

my_car = ElectricCar("Toyota", "Urban Cruiser" , "50kwh")

parent_car = Car("Toyota", "Urban Cruiser")

print(my_car.fuel_type())
print(parent_car.fuel_type("Petrol"))
    