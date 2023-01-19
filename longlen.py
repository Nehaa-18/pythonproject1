long=input("Enter the list :")
max=len(long[0])
temp=long[0]
for ele in long:
    if(len(ele)>max):
        max=len(ele)
        temp=ele
print(long)


