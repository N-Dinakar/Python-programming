month=input("enter the month: ")
date=int(input("enter the date: "))
if month in ("Dec","Jan","Feb","Mar"):
    season = "winter"
elif month in ("Mar","Apr","May","Jun"):
    season = "summer"
elif month in ("Jul","Aug","Sep"):
    season = "spring"
else:
    season = "fall"
if  (date>=20):
    print(season)
elif (date>=21):
    print(season)
elif (date>=22):
    print(season)
elif (date>=21):
   print(season)

