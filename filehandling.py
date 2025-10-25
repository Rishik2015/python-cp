# file=open("demo.txt","r")
# print(file.read())
# file.close()

# fw=open("demo.txt","w")
# fw.write("\n this file  write mode.")
# fw.write("\n now file will  be overriten.")
# fw.close()

# file=open("demo.txt","r")
# print(file.read())

# file.close()

# read parts

# file=open("demo.txt")
# print(file.read(19))
# file.close()

# read lines
# file=open("demo.txt")
# print(file.readline())
# print(file.readline())
# print(file.readline())

# file.close()

# file=open("demo.txt")
# for i in file:
#     print(i)

# file.close()

#removing files with prefix

# file1 = open('demo.txt','r')

# file2 = open('demoUpdated.txt','w')

# for line in file1.readlines():
#     if not(line.startswith("Coding")):
#         print(line)
#         file2.write(line)
# file1.close()      
# file2.close()  

# with open ("demo.txt","a") as f:
#     f.write("hello world")
# with open ("demo.txt","r")  as f:
#     print(f.read())  
#     f.close()

# with open ("demo.txt","r") as file :
#     data = file.readlines()
#     print ("Words in this file are..................")
#     for line in data :
#         word = line.split()
#         print(word)
# file.close()


# new_file = open ("newpy.txt","x")
# new_file.close()

import os
if os.path.exists('newpy.txt'):
     os.remove("newpy.txt")
else:
     print("the file does not exist")
    

