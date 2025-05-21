# 8. The super() Function
# Assignment:
# Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.



#Step 01 : Parent Class
class Person:
    def __init__(self, name):
        self.name = name
       

#Step 02 : Child Class
class Teacher(Person): #inherit person class
    def __init__(self, name, subject):
        super().__init__(name)  #Super func Call the constructor of the parent class
        self.subject = subject 

#Step 03 : display
    def display(self):
        print(f"Name: {self.name}, Subject: {self.subject}")
       
#Creating an object of the child class
if __name__ == "__main__":
    teacher = Teacher("Maha", "Python")
    teacher.display()
