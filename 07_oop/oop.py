# class Car:
#     # __init__ is constructor
#     def __init__(self,userbrand,usermodel):
#         self.brand = userbrand
#         self.model = usermodel

#     def full_name(self):
#         return f"{self.brand} {self.model}"
# Encapsulation
# class Car:
#     # after adding __ it is private
#     total_car = 0
#     def __init__(self,userbrand,usermodel):
#         self.__brand = userbrand
#         self.model = usermodel
#         Car.total_car +=1

#     def full_name(self):
#         return f"{self.__brand} {self.model}"
    
#     def get_brand(self):
#         return self.__brand + "!"
    
#     def fuel_type(self):
#         return "Petrol or Diesel"
#     # Decorators
#     @staticmethod
#     def general_description():
#         return "Cars "


class Car:
    # Use a property decorator in the Car class to make the model attribute read-only.
    total_car = 0
    def __init__(self,userbrand,model):
        self.__brand = userbrand
        self.__model = model
        Car.total_car +=1

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def get_brand(self):
        return self.__brand + "!"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    # Decorators
    @staticmethod
    def general_description():
        return "Cars "
    
    @property
    def model(self):
        return self.__model

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"

my_car = Car("Toyota","Corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.fuel_type())
# print(my_car.full_name())
# my_new_car = Car("Tata","Safari")
# print(my_new_car.brand)
# print(my_new_car.model)

my_tesla = ElectricCar("Tesla","Model S","85Kwh")

# print(my_tesla.__brand)
# print(my_tesla.get_brand())
# print(my_tesla.fuel_type())
# print(my_tesla.model)
# print(my_tesla.full_name())
# print(my_tesla.battery_size)
# print(my_tesla.total_car)
# print(my_tesla.general_description())
# print(Car.total_car)
# print(Car.general_description())

my_car = Car("Tata","Safari")
# my_car.model="City" after @property decorator gives error
print(my_car.model) # after @property decorator we can access it as a variable and it is also read-only now

print(isinstance(my_tesla,Car))
print(isinstance(my_tesla,ElectricCar))

class Battery:
    def batter_info(self):
        return "This is battery"
class Engine:
    def engine_info(self):
        return "This is engine"

class ElectricCarTwo(Battery,Engine,Car):
    pass

my_new_tesla_two = ElectricCarTwo("Tesla","Model S New")
print(my_new_tesla_two.batter_info())
print(my_new_tesla_two.engine_info())