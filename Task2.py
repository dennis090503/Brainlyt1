class Animal:
    def speak(self):
        pass  # Polymorphism: Method to be overridden by subclasses
class Dog(Animal):
    def speak(self):
        return "Woof!"
class Cat(Animal):
    def speak(self):
        return "Meow!"
class Data:
    def __init__(self, value):
        self.__value = value  # Encapsulation: Private attribute

    def get_value(self):
        return self.__value

    def set_value(self, value):
        if isinstance(value, int):
            self.__value = value
        else:
            print("Value must be an integer.")
# Polymorphism
animals=[Dog(),Cat()]
for animal in animals:
    print(animal.speak())
# Encapsulation
data=Data(10)
print("Initial value:", data.get_value())
data.set_value(20)
print("Updated value:", data.get_value())
data.set_value("Hello")
