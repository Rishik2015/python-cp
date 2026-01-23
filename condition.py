#write a program to check whether the given number is positive?


# number=int(input("enter a number"))

# if number>0:
#     print("it is a positive number.")
# elif number==0:
#     print("it is neutral number")   
# else:
#     print("it is a negative number")  

#WAP to check whether a number entered by the user is divisible by 3 and 5 or both 

# number=int(input("enter a number"))  

# if number%3==0 and number%5==0:
#     print("it is divisible by both")
# else:
#     print("it is not divisible by both")    
     

num1=int(input("enter  cost price"))
num2=int(input("enter  selling price"))

if num1>num2:
    loss=num1-num2
    print("it is a loss.")
    print("loss= ",loss)
else:
    profit=num2-num1
    print("it is a profit")
    print("profit= ",profit)
  


    