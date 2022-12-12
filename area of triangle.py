#find the area of the triangle
a=float(input("Enter the value for a:"))
b=float(input("Enter the value for b:"))
c=float(input("Enter the value for c:"))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("The area of the triangle is:",area)

