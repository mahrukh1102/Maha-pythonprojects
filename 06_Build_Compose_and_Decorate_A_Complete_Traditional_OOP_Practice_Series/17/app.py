# 17. Class Decorators
# Assignment:
# Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!". Apply it to a class Person.



def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
#adding the greet method to the class
    cls.greet = greet
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name
    
    def say_hello(self):
        return f"Hello, My name is {self.name}!"

person1 = Person("Maha")
print(person1.greet())
print(person1.say_hello())