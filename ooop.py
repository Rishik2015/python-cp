#Write a program to create a class with the name Student and perform the following tasks - 1. Declare a variable grade 2. Print a sentence inside the class 3. Create an object of class student and see the output

# class student:
#     grade = 10
#     print("i am studying in grade",grade)

# s1 = student()    

#Write a program to create a class Vehicle and perform the following tasks - 1. Create an __init__ method with arguments - max_speed and mileage 2. Create an object of class Vehicle and pass the maximum speed and mileage of the car 3. Print the values of max_speed and mileage by using the object


# class vehicle:
#     def __init__(self, max_speed,mileage):
#         self.max_speed = max_speed
#         self.mileage = mileage
# modelX = vehicle(240,18)      
# print("Model Max Speed :",modelX.max_speed)  
# print("Model Mileage :",modelX.mileage)

class bankaccount:
    def __init__(self,name,balance=0):
        self.name = name
        self.balance = balance
    def deposit(self , amount) :
        self.balance += amount
        print(f"Deposited ${amount}.New balance : ${self.balance}")   
    def withdraw(self,amount)    :
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}.New balance : ${self.balance}")
        else:
            print("Insufficient funds")    
account1 = bankaccount("john",500)        
account1.deposit(200)    
account1.withdraw(100)
account1.withdraw(700)

account2 = bankaccount("jane")        
account2.deposit(300)    
account2.withdraw(50)
        

