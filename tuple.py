# tup1=(1,2,3,4,6,7)
# print(tup1[3])
# #single element tuple
# tup2=("Rishik",)
# print(type(tup2))

# #changing into lists

# tup3=list(tup1)
# print(tup3)
# tup3[4]=5
# tup3[5]=6
# print(tup3)

# tup1=tuple(tup3)
# print(tup1)

d1={'name':'rishik','grade':5,'pass':True}
print(d1)
print(d1.keys())
print(d1.values())
print(d1.items())

d1["name"]="Rishik pathak"
d1["roll no."]=33


d1.pop("pass")
print(d1)