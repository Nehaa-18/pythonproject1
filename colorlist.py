c1=input("Enter the first group of colors : ").split(',')
c2=input("Enter the second group of colors : ").split(',')
x=(set(c1).difference(c2))
print(x)