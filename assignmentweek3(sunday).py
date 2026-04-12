listt=[11,5,76,3,6,7,89]
x=int(input('enter the numer you want to search about it'))
#order
listt.sort()
#left
start=0
#rigth
end=len(listt)-1
#loop
for i in range(len(listt)):
    #mid point
    mid=(start+end)//2
    if listt[mid]==x:
      print('found at index',mid)
      break
    elif x>listt[mid]:
      start=mid+1
      
    else:
        end=mid-1
     
else:
     print('not found')
        

