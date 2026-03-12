# Write a program to create a function name well wishes that will give output hello, how are you

# def wellwishes():
#     print("hello")
#     print("how are you?")

# wellwishes()

# Write a program to make a calculator : For making a calculator create four functions add, subtract, multiply, divide. Ask for a choice from users which operation they want to perform. Take user input whatever operation they want to perform And call that function accordingly.


def add(p,q):
    return p+q
def subtract(p,q):
    return p-q
def multiply(p,q):
    return p*q
def divide(p,q):
    return p/q

print("please select the operation")
print("a.ADDITION")
print("b.SUBTRACTION")
print("c.MULTIPLICATION")
print("d.DIVISION")

choice = input("please chose the option a./b./c./d. ")

num_1=int(input("please enter your first number "))
num_2=int(input("please enter your second number "))

if choice=='a':
    print(num_1,"+",num_2,"=",add(num_1,num_2))
elif choice=='b':
    print(num_1,"-",num_2,"=",subtract(num_1,num_2)) 
elif choice=='c':
    print(num_1,"*",num_2,"=",multiply(num_1,num_2))  
elif choice=='d':
    print(num_1,"/",num_2,"=",divide(num_1,num_2))      
else:
    print("invalid input")      
    