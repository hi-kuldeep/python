class Car:
    total_car = 0
    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand_name(self):
        return f"Brand: {self.__brand}"

    def fuel_type(self , type):
        return type

    @staticmethod
    def get_description():
        return "This is a just learning class!"

    @property
    def model(self):
        return self.__model

    # @property
    # def brand(self):
    #     return self.__brand

class ElectricCar(Car):
    def __init__(self , brand , model , battery_size):
        super().__init__(brand , model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"
    

my_car = ElectricCar("Toyota", "Urban Cruiser" , "50kwh")

parent_car = Car("Toyota", "Urban Cruiser")


# my_car.model = "12321" # this is gives error because model is now readonly

print(my_car.model)

