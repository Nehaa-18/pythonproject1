a=3
odd=0
even=0
while(a<=100):
    if(a%2==1):
        odd=odd+a
    else:
        even=even+a
    a=a+1
print("Sum of odd is :",odd)
print("Sum of even is :",even)