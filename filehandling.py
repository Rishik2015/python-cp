# file=open("demo.txt","r")
# print(file.read())
# file.close()

fw=open("demo.txt","w")
fw.write("\n this file  write mode.")
fw.write("\n now file will  be overriten.")
fw.close()

file=open("demo.txt","r")
print(file.read())

file.close()
