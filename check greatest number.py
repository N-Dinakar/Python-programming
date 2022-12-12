#program to find the greatest of three number
n1=int(input("Enter the value for n1"))
n2=int(input("Enter the value for n2"))
n3=int(input("Enter the value for n3"))
if (n1>n2)and(n1>n3):
    print("n1 is the greatest number")
elif(n2>n3)and(n2>n1):
        print('n2 is the greatest number')
else:
            print('n3 is the greatest number')
