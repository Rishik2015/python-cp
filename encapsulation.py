# Write a program to create a class with following variables and methods - 1. Private variable named privateVar that contains an integer value 2. Create a private function privMeth that prints a message 3. Create a function hello that prints the value of privateVar 4. Create an object for the class and call all the function

# class myClass:
#     __privateVar = 27;
#     def __privMeth(self):
#         print("I AM INSIDE MY CLASS SILLY GOOSE")
#     def hello(self)    :
#         print("Private variable value : ", myClass.__privateVar)


# goo = myClass()
# goo.hello()
# goo.__privMeth

# class Student:
#     def __init__(self , name , marks):
#         self.name = name
#         self.__marks = marks
#     def get_marks(self) :
#         return self.__marks



#     def display(self) :
#         print(f"Name: {self.name}, Marks:{self.__marks}")  

# s1 =   Student("Rahul",85) 
# print(s1.name)       
# print(s1.get_marks)
# s1.display()

class Number:
    def __init__(self ,value):
        self.value = value

    def __eq__(self , other)    :
        return self.value ==    other.value
    
n1 = Number(10) 
n2 = Number(4)   
print(n1 == n2)