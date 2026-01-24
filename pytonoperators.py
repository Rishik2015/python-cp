# r=7
# m=22
# c=0

# if r and m and c:
#     print("all the numbers have boolean value as true.")
# else:
#     print("atleast one number has boolean value as false.")    

# x=7
# y=-7
# z=0

# if x > 0 or y > 0:
#     print("either of the number is greater than 0")
# else:
#     print("no number is greater than 0")    


# if y > 0 or c > 0:
#     print("either of the number is greater than 0")    
# else:
#     print("no number is greater than 0") 
# 
# Write a program to calculate the BMI of a person?

height=float(input("enter your height in metres"))  
weight=float(input("enter your weight in kilograms")) 

bmi= weight/height**2

print("your BMI is",bmi)

if bmi <= 18.4:
    print("you are underweight")
elif bmi <= 24.9:
    print("you are healthy")
elif bmi <= 29.9:
    print("you are overweight")
elif bmi <=34.9:
    print("you are obese")  
else:
    print("you are severely obese")    


