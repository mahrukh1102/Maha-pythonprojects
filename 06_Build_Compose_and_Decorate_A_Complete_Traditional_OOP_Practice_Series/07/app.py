# 7. Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.





class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name #Public
        self._salary = salary #Protected
        self.__ssn = ssn #Private

if __name__ == "__main__":
    emp = Employee("Maha", 6000, "123-456-789")
    #now we can access the public variable
    print("Public variable: ", emp.name)
    #now we can access the protected variable   
    print("Protected variable: ", emp._salary)
    

    #we can access the private variable using try catch
    try:
        print("Private variable: ", emp.__ssn)
    except AttributeError :
        print("Cannot access private variable __ssn")