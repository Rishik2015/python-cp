#Write a program to understand how the value error exception works?
# try:
#     number= int(input("enter a number"))
#     print("the number entered is ",number)
# except ValueError as ex:
#     print("exception")

#Write a program to check how the exceptions and finally statement works

# try:
#     num1,num2 = eval(input("enter 2 numbers seperated by a comma : "))
#     result = num1 / num2
#     print("Result is ",result)
    
# except ZeroDivisionError:
#     print("Division by zero is error !!!!!!!!!!!!!!!!!")
# except SyntaxError:
#     print("Enter number seperated by a commma like this 6,7")   
# except:
#     print("wrong input")    
# else:
#     print("no exceptions")    
# finally:
#     print("THIS WILL EXECUTE NO MATTER WHAT HAPPENS")

valid = False
while True:
     try:
         n=int(input("enter a number"))
         while n%2==0:
             print("bye")
             valid=True
     except ValueError:
         print("invalid")