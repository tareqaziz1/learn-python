# Class
'''
We use classes to define types.

A class is like a blueprint for creating objects
because it defines the structure and behavior that 
every object created from it will have. 
Just like a blueprint of a house shows 
what rooms, doors, and windows the house will have, 
a class describes what data (attributes) and actions (methods) an object should contain. 
When you create an object from a class, you are making a real instance based on that design, 
with its own values but the same structure. 
This makes code more organized, reusable, and easier to manage as programs grow.
'''

class Car:                            # Creating a Blueprint for car.
    def __init__(self, brand, year):  # Constructor for Class
        self.brand = brand            # It takes the values passed in (brand, year) and stores them inside the object.
        self.year = year

    def drive(self):
        print(f"the brand is {self.brand} {self.year} and it is driving!")  #output- the brand is Tesla 2026 and it is driving!.

# Making 2 car objects

car1 = Car("Tesla", 2026)
car2 = Car("Toyota", 2020)


print(car1.brand)
print(car2.brand, car2.year)

car1.drive()

class Triangle:
    def move(self):
        print("Move")

    def draw(self):
        print("Draw")

triangle1 = Triangle()
triangle1.x = 10
triangle1.y = 15
triangle1.z = 20

print(f"x = {triangle1.x} , y = {triangle1.y} and z = {triangle1.z}")


class Points:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def add_axis(self):
        addition = self.x + self.y
        return addition



point1 = Points(5.5, 2.3)
point2 = Points(2.1, 3.3)

print(point1.add_axis())
print(point2.add_axis())

point1.x = 50
print(point1.x) #output- 50

# inheritance
# inheritance means a class can copy and use the features (variables and functions) of another parent class.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def talk(self):
        print(f"Hi, I am {self.name} and I am {self.age} years old.")


person1 = Person("John", 30)

person1.talk()

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print(f"{self.brand} is starting!")

    def stop(self):
        print(f"{self.brand} is stopped!")

class BMW(Vehicle):       # BMW will inherit all the methods and variables from the Vehicle class.
    pass                    # Python does not recommend an empty class. "Pass"keyword is used to pass the line.


bmw1 = BMW("bmw", 2020)

bmw1.start()
bmw1.stop()

class Ford(Vehicle):
    def engine(self, isGood):
        self.isGood = isGood
        print(f"it is good {isGood}")

ford1 = Ford("Ford", 2025)
ford1.start()
ford1.engine(True)    # Now ford1 object has inherited methods (start, stop) and also its own method (engine).




