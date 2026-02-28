# Write a program to check how many times a character is repeated in a word?

# string= input("please enter your own word :   ")
# char = input("please enter your charecter  ")
# i= 0
# count= 0

# while(i < len(string)):


#     if(string[i] == char):
#         count = count+1

#     i=i+1

# print("the total number of times  ",char," has occured =  ",count)

#Write a program to print all the prime numbers which come in the range entered by the user?

lower = int(input("enter a lower range"))
upper = int(input("enter a upper range"))

print("prime between ",lower,"and",upper,"are:")

for num in range(lower,upper+1):
    if num>1:
        for i in range(2, num):
            if (num % i)==0:
                break
        else:
            print(num)    





