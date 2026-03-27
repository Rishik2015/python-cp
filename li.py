#Write a program to perform the following operations on a List: 1. Create an empty list 2. A list with elements 3. Use * operator 4. Reverse a list

# empty_list = []
# print()

# numbers = [6,4,22,6,7]
# print(numbers)

# triples = [6,4,22] * 3
# print(triples)

# alist = [163,123,67,22,6]
# alist = alist[::-1]
# print(alist,"\n")

#Write a Python program to count the number of strings where the string length is two or more, and the first and last characters are the same from a given list of strings

def match_words(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)
    print("List of words with with first and last characters same\n",lst)    
    return ctr 
count = match_words(['minu','vikram','rishik','67','1221'])   
print("number of words having first and last lettter same",count)