#Write a program to check whether the given tuple - (1,2,3,3,2,1) is a palindrome or not. If it's a palindrome, then it is the same after being reversed.

# def palind(r):
#     e = len(r) -1
#     s = 0
#     while(s<e):
#         if(r[s]!=r[e]):
#             return False
#         s+=1
#         e-=1
#     return True
# r = (1,2,3,2,1) 

# if(palind(r)):
#     print("the tuple is flipflop")
# else:
#     print("the tuple is not flipflop")  
# 
# Create a tuple named weather with these elements - (1, 0, 0, 0, 1, 1, 0). If the element is 1 then the value of rainy increases by 1 otherwise the value of sunny increases by 1. On the basis of the value of rainy and sunny, predict the weather.

weather = (1,0,0,0,1,1,0)
sunny = 0
rainy = 0
for i in range(0,7):
    if(weather[i]==1):
        rainy+=1
    else:
        sunny+=1
if(sunny>rainy):
    print("goodu weathera")      
else:
    print("baddu weathera")    