a=int(input("Enter the number of the new loaves purchased:"))
b=int(input("Enter the number of the old loaves purchased:"))
c=185.00
anl=(a*c)
aol=(c*60/100)
d=(c-aol)*b
tm=d+anl
print("Regular price:Rs.",c)
print("Amount of new loaves:",anl)
print("Amount of day old loaves:",d)
print("Total amount:Rs.",tm)
