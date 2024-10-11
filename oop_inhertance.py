#----------------------------------------------------------------
# class super_class:
#     # attributes and method definition
#     ...
# class sub_class(super_class):
#     # attributes and method of super_class
#     # attributes and method of sub_class
#     ...
#---------------------------------------------------------------
class Animal:
    # attribute and method of the parent class
    name = ""

    def eat(self):
        print("i can eat")


# inherit from Anima
class Dog(Animal):

    # new method in subclass
    def display(self):
        return f"My name is {self.name}"


labrador = Dog()
labrador.name = "max"
labrador.eat()
print(labrador.display())

#-------------------------------------------------------------------
# class Car:
#     car_name=""
#
#     def vehicle(self):
#         print("i have 4 balon")
#
# class mers(Car):
#
#     def display(self):
#         return f"My name is {self.car_name}"
#
# mersedes=mers()
# mersedes.car_name="gls"
# mersedes.vehicle()
# print(mersedes.display())

#-------------------------------------------------------------------
# class Transport:
#     def __init__(self, name, speed, color, engine: bool):
#         self.name = name
#         self.speed = speed
#         self.color = color
#         self.engine = engine
#
#     def move(self):
#         if self.engine:
#             return "car is moving"
#         else:
#             return "car isn't moving"
#
#     def drive(self):
#         print("i am driving")
#
#     def show_info(self):
#         print(f"nomi:{self.name}\ntezligi:{self.speed}\nrangi:{self.color}\nengine:{self.engine}")
#
#
# class Car(Transport):
#     def __init__(self, name, speed, color, engine, distance_covered):
#         super().__init__(name, speed, color, engine)
#         self.distance_covered = distance_covered
#
#     def drive(self):
#         super().drive()
#         print("Mashina yo'lda yurayapti")
#
#     def show_info(self):
#         super().show_info()
#         print("mashina hali yangi yurgan masofa=0")
#
#
# class Bicycle(Transport):
#
#     def pedal(self):
#         print("Pedal aylantiryapman")
#
#
# car1 = Car("mers", 170, "black", True, 50)
#
# print(car1.show_info())
