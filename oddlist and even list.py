n=int(input("Enter the number N:"))
sum=0
even=0
odd=0
evenlist=[]
oddlist=[]
for i in range(1,n+1):
    if i%2==0:
        even=even+i
        evenlist.append(i)
    else:
        odd=odd+i
        oddlist.append(i)
        sum=sum+i+5
print("sum of ",n,"number is :",sum)
print('sum of odd number is :',odd)
print("sum of even number is :",even)
print("odd list:",oddlist,"even list:",evenlist)
