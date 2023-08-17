num1=int(input("emter first number: "))
num2=int(input("enter second number: "))
op=input("Enter any operators you want(+,-,*,/)): ")
if op=="+":
    print(num1+num2)
elif op=="-":
    print(num1-num2)
elif op=="/":
    print(num1/num2)
elif op=="*":
    print(num1*num2)
else:
    print("enter valid operators")