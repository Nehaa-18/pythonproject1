list1=[12,16,34,56,23]
list2=[24,54,76,22,15]
x=len(list1)
y=len(list2)
a=sum(list1)
b=sum(list2)
if(x==y):
    print("Lists are same")
else:
    print("lists are different")
if(a==b):
    print("Sum of lists are same")
else:
    print("Sum of lists are different")
print("Common elements:")
for i in list1:
    for j in list2:
        if(i==j):
            print(i)