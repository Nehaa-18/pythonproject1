lis=[]
n=int(input("Enter the number:"))
print("Enter the words:")
for i in range(0,n):
    y=input()
    lis.append(y)
def longest(lis):
    return max(lis,key=len)
print("Longest word is :"+longest(lis)+"  ")
print(len(longest(lis)))