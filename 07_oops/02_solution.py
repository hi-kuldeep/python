class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    
    def full_name(self):
        return f"Brand: {self.brand}, Model: {self.model}"

my_car = Car("Toyota", "Urban Cruiser")

print(my_car.full_name())
    
    