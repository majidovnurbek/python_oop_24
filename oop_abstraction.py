from abc import ABC ,abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

    def sleep(self):
        print("animal is sleeping")

class Dog(Animal):
    def sound(self):
        print("woof woof")

class Cat(Animal):
    def sound(self):
        print("Moow")

dog=Dog()
cat=Cat()

dog.sound()
dog.sleep()
cat.sleep()
cat.sound()