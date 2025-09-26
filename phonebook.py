import sys

def initial_phonebook():
    rows, cols = int(input("Please add your initial number of contacts :")),5

    phone_book = []
    print(phone_book)
    for i in range(rows):
        print("\nEnter contact %d details in the following order (ONLY):"% (i+1))
        print("NOTE: * indicates mandatory fiels")
        print("............................................................")
        temp = []
        for j in range(cols):
            if j== 0:
                temp.append(str(input("Enter name*:")))
                if temp[j]  == ' ' or temp[j]=='':
                    sys.exit("name is a mandatory fielld.process exiting due to blank field")
            if j== 1:
                temp.append(int(input("Enter number*:")))  
            if j== 2:
                temp.append(str(input("Enter email adress:")))
                if temp[j]  == ' ' or temp[j]=='':  
                    temp[j]  = None
            if j== 3:
                temp.append(str(input("Enter date of birth*:"))) 
                if temp[j]  == ' ' or temp[j]=='':  
                    temp[j]  = None
            if j== 4:
                temp.append(str(input("Enter date of birth*:"))) 
                if temp[j]  == " " or temp[j]=='':  
                    temp[j]  = None
        phone_book.append(temp)            
    print(phone_book)
    return phone_book

