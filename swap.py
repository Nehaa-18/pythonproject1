#program to swap two numbers

#enter two numbers
fn=int(input("enter the first number"))
sn=int(input("enter the second number"))
#declare a temperary variable
temp=fn
fn=sn
sn=temp
#print the swapped numbers
print("After swapping the numbers are")
print("The first number=",fn)
print("The second number=",sn)