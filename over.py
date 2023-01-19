n=int(input("Enter the size :"))
print("Enter the elements :")
list=[]
for i in range(0,n):
    ele=int(input())
    if(ele>100):
        list.append("over")
    else:
        list.append(ele)
print(list)
