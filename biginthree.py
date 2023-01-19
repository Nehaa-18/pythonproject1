a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
def max(a,b,c):
    if(a>=b)and (a>=c):
        biggest=a
    elif(b>=a)and(b>=c):
        biggest=b
    else:
         biggest=c
    return biggest
print("The biggest number is :")
print(max(a,b,c))