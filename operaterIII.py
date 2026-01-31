#Write a program to illustrate the use of 'is' identity operator

r=31
if (type(r)is int):
    print("true")
else:
    print("false")
ri=398.77
if (type(ri)is not float ) :
    print("true")   
else:
    print("false")  
x= 77
y= 77
if (x is y):
    print("it is same identity")
y=45
if(x is not y):
    print("both are different")

#Write a program to apply the right shift and left shift bitwise operator.

a=10
b=-10

print("a>>1 =",a>>1)
print("b>>1 =",b>>1)

a=5
b=-10

print("a<<1 =",a<<1)
print("b<<1 =",b<<1)







