a=int(input("Enter the first number :"))
b=int(input("Enter the second number :"))
choice=int(input("Enter the choice(1/2/3/4) :"))
print("1 : Add")
print("2 : Subtract")
print("3 : Multiple")
print("4 : Divide")
if(choice==1):
    print("After addition the number is :",a+b)
elif(choice==2):
    print("After subtraction the number is :",a-b)
elif(choice==3):
    print("After multiplication the number is :",a*b)
elif(choice==4):
    print("After division the number is :",a/b)
else:
    print("Invalid choice")


