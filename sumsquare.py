l=[22,3,46,77,86,55]
def sumsquare(l):
 odd=0
 even=0
 evenlist=[]
 oddlist=[]
 for i in l:
     if i%2==0:
        even=even+i**2
        evenlist.append(even+i**2)
     else:
        odd=odd+i**2
        oddlist.append(odd+i**2)
 l=[oddlist,evenlist]
 return(l)
print(sumsquare(l))


    
