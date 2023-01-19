r1=int(input("Enter the range 1 :"))
r2=int(input("Enter the range 2 :"))
for num in range(r1,r2 +1):
    # order of number
    order=len(str(num))
    #initialize sum
    sum=0

    temp=num
    while temp>0:
        digit=temp%10
        sum+=digit**order
        temp//=10

    if num==sum:
        print(num)