word=input("Enter the string :")
x={}
count=0
str1=word.split()
for i in str1:
    if i in x:
        x[i]+=1
    else:
        x[i]=1
print("Character occurance :")
for j,k in x.items():
    print(j,k)