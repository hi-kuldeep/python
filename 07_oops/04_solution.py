class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model

    def get_brand_name(self):
        return f"Brand: {self.__brand}"

class ElectricCar(Car):
    def __init__(self , brand , model , battery_size):
        super().__init__(brand , model)
        self.battery_size = battery_size

    # def electric_car_name(self):
    #     return f"Brand: {self._Car__brand}, Model: {self.model}, Battery Size: {self.battery_size}"
    

my_car = ElectricCar("Toyota", "Urban Cruiser" , "50kwh")

print(my_car.electric_car_name())
print(my_car.battery_size)
print(my_car.get_brand_name())
    