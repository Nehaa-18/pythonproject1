list1=[12,23,-7,43,32,2]
list2=[3,76,-19,14,2,53]
x=len(list1)
y=len(list2)
s1=sum(list1)
s2=sum(list2)
if(x==y):
    print("List are of same length")
else:
    print("List are of different length")
if(s1==s2):
    print("Sum of two list are same")
else:
    print("Sum is different")
    print("Common elements")
for i in list1:
    for j in list2:
        if(i==j):
            print(i)