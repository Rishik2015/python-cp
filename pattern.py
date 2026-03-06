# Write a program to demonstrate a right angle triangle pattern?

# print("HALF PYRAMID PATTERN OF DOLLAR($)")
# n=int(input("enter the number of rows:   "))
# for i in range(n):
#     for j in range(i+1):
#         print("$ ",end="")
#     print()

# rows=int(input(" enter the total number of rows "))
# number= 1
# print("FLOYD'S TRIANGLE")
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print(number,end=' ')
#         number=number+1
#     print()  

n=int(input("enter the number of rows"))  
for i in range(n,0,-1):
    for j in range(1,i+1):
        print("/",end= " ")
    print()    
