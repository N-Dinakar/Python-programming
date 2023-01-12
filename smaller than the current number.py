n=int(input("Enter the number of items in list:"))
l1=[]
for i in range(n):
    a=int(input("Enter the number:"))
    l1.append(a)
print(l1)
l2=[]
for i in l1:
    count=0
    min=i
    for j in l1:
        if min>j:
            count=count+1
        else:
            continue
    l2.append(count)
print(l2)
