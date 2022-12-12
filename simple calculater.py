a=float(input("Enter the value for a:"))
b=float(input("Enter the value for b:"))
print("slection")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
while True:
    choice=input("Enter the choice:")
    if choice in['1','2','3','4']:
        num1=a
        num2=b
        if choice=='1':
            print('addition of the two numbers is:',num1+num2)
        elif choice=='2':
            print('subtraction of the two numbers is:',num1-num2)
        elif choice=='3':
            print('multiplication of the two numbers is:',num1*num2)
        else:
            print('division of the two number is :',num1/num2)
        break
