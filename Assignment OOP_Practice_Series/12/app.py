# 12. Static Methods
# Assignment:
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.



class TemperatureConverter():

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32
    
if __name__ == "__main__":
    print("Fahrenheit:", TemperatureConverter.celsius_to_fahrenheit(0))
    print("Fahrenheit:", TemperatureConverter.celsius_to_fahrenheit(200))
