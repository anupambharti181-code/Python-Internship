# Simple Calculator Project
# Taking input from the user
num1=float(input("enter first number:"))
num2=float(input("enter second number:"))

print("1.addition(+)")
print("2.subtraction(-)")
print("3.multiplication(*)")
print("4.division(/)")

choice=input("enter your choice(1-4:)")

if choice=="1":
    print("result:",num1+num2)

elif choice=="2":
    print("result",num1-num2)

elif choice=="3":
    print("result",num1*num2)

elif choice=="4":
    if num2!=0:
        print("result:",num1/num2)
    else:
        print("cannot divide by zero!")

else:
    print("invalid choice!")                    