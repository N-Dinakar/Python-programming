math=int(input("enter the mark for math"))
python=int(input("enter the mark for python"))
eng=int(input("enter the mark for english"))
average=math+python+eng/100
if (average>90):
    print("grade is a")
elif(average>70):
        print("grade is b")
elif(average<50):
            print("grade is fail")
