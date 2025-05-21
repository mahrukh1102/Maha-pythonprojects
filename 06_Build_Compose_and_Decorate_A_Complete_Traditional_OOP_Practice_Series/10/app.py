# 10. Instance Methods
# Assignment:
# Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including the dog's name.


class Dog:
    def __init__(self, name, breed):
        self.breed = breed #instance variable
        self.name = name #instance variable

    def bark(self):
        print( f"{self.name} is barking!")

if __name__ == "__main__":
    #Creating (Object)instances of the Dog class
    dog1 = Dog("Duggo", "Husky")
    dog2 = Dog("Sasha", "Golden Retriever")
    
    #Calling the methods
    dog1.bark()
    dog2.bark()