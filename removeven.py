n=int(input("Enter the size of list :"))
print("Enter the elements :")
list=[]
for i in range(0,n):
    x=int(input())
    if(x%2!=0):
        list.append(x)
print("Odd numbers are :",list)
