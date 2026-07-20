class Car:
    def __init__(self , brand , model , year):
        self.__brand = brand
        self.__model = model
        self.__year = year

class Battery:
    def __init__(self , battery_type , capacity):
        self.battery_type = battery_type
        self.capacity = capacity
    
    def get_battery_info(self):
        return self.battery_type + " " + self.capacity

class Engine:
    def __init__(self , engine_type , capacity):
        self.engine_type = engine_type
        self.capacity = capacity
    def get_engine_info(self):
        return self.engine_type + " " + self.capacity

class ElectricCarTwo(Car , Battery , Engine): 
    def __init__(self , brand , model , year , battery_type , capacity , engine_type):
        super().__init__(brand , model , year)
        Battery.__init__(self, battery_type, capacity)
        Engine.__init__(self, engine_type, capacity)

car_info = ElectricCarTwo("Tata" , "Nexon" , 2024 , "Lithium ion" , "60kwh" , "Electric Motor")
print(car_info.get_battery_info())
print(car_info.get_engine_info())