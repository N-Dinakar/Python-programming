year=int(input("Enter the year:"))
y=year%4
z=year-(y-4)
if (year%400==0)and(year%100==0):
    print(year,"is an leap year")
elif (year%4==0)and(year%100!=0):
    print(year,"is an leap year")
else:
    print("The given year is not a leap year and",z,"is the next leap year")

    
   
