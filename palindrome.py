num=int(input("Enter a number:"))
temp=num
rev=0
while(num>0):
        d = num % 10
        rev = rev * 10 + d
        num //= 10
if(temp==rev):
        print("It is a palindrome")
else:
    print("Not a palindrome")