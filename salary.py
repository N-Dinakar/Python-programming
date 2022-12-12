a=int(input("Enter your salary:"))
s=str(input("ENter your sex male or female:"))
if (s=="male"):
    print("your bonous due to diwali :"+"Rs.", a*(5/100),"salary is :",a+(a*(5/100)))
if (s=="female"):
    print("Your bonous due to diwali :"+"Rs.", a*(10/100),"salary is :",a+(a*(10/100)))
if (s=="male" and a<10000):
     print("And also based on your salary:"+"Rs.", (a*(7/100)))
     print("Total salary is :",a+(a*(7/100)))
if (s=="female" and a<10000):
    print("And also based on your salary:"+"Rs.", (a*(12/100)))
    print("Total salary is :",a+(a*(12/100)))
