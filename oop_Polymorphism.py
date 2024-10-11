'''
OOP  Polymorphism: ->  Overloading Overriding : ko'p shakillilik
'''  # noqa
'''
Overloading, bir sinfdagi biror funksiya yoki
metod nomini bir nechta turdagi argumentlar
bilan o'zgartirish imkoniyatini anglatadi. Misol uchun:
'''  # noqa

# Overloading
class Calculate:
    def add(self, x, y):
        return x + y

    def add(self, x, y, z):
        return x + y + z


obj = Calculate()
print(obj.add(1, 2, 3))

# Overriding
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return f"Name: {self.name}\nage: {self.age}"


person1 = Person("Anna", 16)
print(person1.info())


class Child(Person):
    def __init__(self, name, age, year, address):
        super().__init__(name, age)
        self.year = year
        self.address = address

    def info(self):
        return f"Name: {self.name}\nage: {self.age}\nyear: {self.year}\naddress: {self.address}"


child1 = Child("Bekzod", 23, 2001, "Bukhara")
print("")
print("Overriding")
print("")
print(child1.info())
