class Car:
    total_car = 0
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand_name(self):
        return f"Brand: {self.__brand}"

    def fuel_type(self, type):
        return type

    @staticmethod
    def get_description():
        return "This is a just learning class!"

    @property
    def model(self):
        return self.__model


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"


my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
my_car = Car("Toyota", "Urban Cruiser")

# Demonstrate isinstance()
print("Is my_tesla an instance of ElectricCar?:", isinstance(my_tesla, ElectricCar))
print("Is my_tesla an instance of Car?:", isinstance(my_tesla, Car))
print("Is my_car an instance of ElectricCar?:", isinstance(my_car, ElectricCar))
print("Is my_car an instance of Car?:", isinstance(my_car, Car))
