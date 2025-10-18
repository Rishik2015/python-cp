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

file1 = open('demo.txt','r')

file2 = open('demoUpdated.txt','w')

for line in file1.readlines():
    if not(line.startswith("Coding")):
        print(line)
        file2.write(line)
file1.close()      
file2.close()  