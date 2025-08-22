#Write a Python class named Rectangle with a length and width and a method that computes the area of a rectangle. 
# Display the dimensions and calculated area of the rectangle as well.

class rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self) :
        print("Area of Rectangle=",self.length*self.width) 

r1=rectangle(6,5)
r1.area()

## Write a program to create a class Vehicle and perform the following tasks -

# 1. Create an __init__ method with arguments - max_speed and mileage

# 2. Create an object of class Vehicle and pass the maximum speed and mileage of the car

# 3. Print the values of max_speed and mileage by using the object

class vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage
          
    def vehicles(self):
            print("Mileage and Max_speed of a vehicle ", self.mileage,self.max_speed)

v1=vehicle(200,18)
v1.vehicles()