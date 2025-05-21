# 3. Public Variables and Methods
# Assignment:
# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.


class Car:
    def __init__(self, brand):
        self.brand = brand
    
    def start(self):
        print(f"{self.brand} car is starting.")

if __name__ == "__main__":
    my_car = Car("Audi")
    print(my_car.brand)
    my_car.start()