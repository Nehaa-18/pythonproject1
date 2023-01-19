num=int(input("Enter a number :"))
i=2
while(i<=num/2):
    if(num%i==0):
        print("It is a prime number")
i=i+1
else:
    print("It is not a prime number")
