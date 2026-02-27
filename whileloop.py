#Write a program to find the sum of natural numbers.

# bw=int(input("Enter the value of terms"))
# sum=0
# ri=1
# while ri<=bw:
#     sum=sum+ri
#     ri=ri+1

# print("\n sum :  ",sum)   
# 
# Write a program to check the infinite loop?


# i=0
# while i<=0:
#    print("Apollo 13 'We wil fly forever'")

num=int(input("enter a number")) 
sum=0
temp=num
while temp > 0:
    digit=temp%10
    sum+= digit**3
    temp //=10
if num == sum:
    print("the arm strong number is     ",num)
else:
    print(num,"     is not a armstrong number")    
