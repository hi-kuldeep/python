class Car:
    total_car = 0
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1

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
# Recommended: Accessing via Class Name explicitly shows it is a shared Class variable.
# This makes code intent clear to anyone reading it.
print(Car.total_car)

# Not Recommended: Accessing via Instance (my_car) works for reading, but is bad practice.
# DANGER: If you assign `my_car.total_car = 5`, Python creates a NEW instance variable
# on `my_car` that shadows the class variable, leading to subtle bugs!
print(my_car.total_car)