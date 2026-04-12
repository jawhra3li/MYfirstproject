"""
values=["Ali","mohammed",5678,86,76]
print(len(values))
listtest=[]
print(len(listtest))
listtest1=[" "]
print(len(listtest1))
print(values[3])
name=values[0]
print(name[0])
print(values[0][2])
print(values[1][-1])
print(values[1][len(values[1])-1])
print(values[1][len(values[1])-2])
###print(values[1][len(values[1]//2)])
##how store?
values1=[1,2 ]
values1.append(20)
values1.append(30)
values1[1]=5
print(values1)
grades=[]
for i in range(5):
    grade=float(input("enter your grade"))
    grades.append(grade)
print(grades)

for grade in range(len(grades)):
    print(grades[grade])

for grade in grades:
    print(grade)
    

yourlist=[]
yourlistn=input("enter your list nummber")
for yourlistn in range(len(yourlist)):
    yourlist.append(yourlistn)
   

yourlist=[3,2,7,8,10]
index=-1
n=int(input("enter your list nummber"))
for i in range(len(yourlist)):
    if yourlist[i]==n:
        index=i
        break
print(i)
        
listt=[3,2,7,8,10]
summ=0
for i in range(len(listt)):
    summ+=listt[i]
print(summ)

##min max
print(max(listt))
print(min(listt))
##usig loop 
##max
listt=[3,2,7,8,10]
maxx,minn=listt[0],listt[0]
for i in range(len(listt)):
    if listt[i]>maxx:
        maxx=listt[i]
print("max value is",maxx)
for i in range(len(listt)):
    if listt[i]<minn:
        minn=listt[i]
print("min value is ",minn)

listt=[3,2,7,8,10]
for i in range(len(listt)):
    if listt[i]%2!=0:
        odd=listt[i]
        i+=1
        print("odd number is",odd)
        
listt=[3,-2,7,8,10]
for i in range(len(listt)):
    if listt[i]<0:
        ne=listt[i]
        listt[i]=0
        print("new list",listt)
        
listt=[3,3,6,6,-2,7,7,6,8,10]
newLis=[]
for i in range(len(listt)):
    rep=1
    for j in range(i+1, len(listt)):
        if listt[i] in newLis:
            break
        if listt[i]==listt[j]:
            rep+=1
    if rep>1:
        newLis.append(listt[i])
        print("repate number",listt[i],rep,"times")       


   
listtt=[1,2,4,5,7]
tar=3
for i in range(len(listtt)):
    if listt[i+1]+listt[i]==tar:
       print(listt[i+1],listt[i],"given",tar)

listtt=[1,2,4,3,6,8,5,7]
tar=10
for i in range(len(listtt)):
   for j in range(i+1, len(listtt)):
       for y in range(j+1,len(listtt)):            
          if listtt[i]+listtt[j]+listtt[y]==tar:
             print(listtt[i],listtt[j],listtt[y],"given",tar)
        

listtt=[1,2,4,3,6,8,5,7]
tar=int(input('enter your target'))
for i in range(len(listtt)):
   for j in range(i+1, len(listtt)):
       for y in range(j+1,len(listtt)):            
          if listtt[i]+listtt[j]+listtt[y]==tar:
             print(listtt[i],listtt[j],listtt[y],"given",tar)
"""

listt=[3,3,6,6,-2,7,7,6,8,10]
newLis=[]
for i in range(len(listt)):
    rep=1
    for j in range(i+1, len(listt)):
        if listt[i] in newLis:
            break
        if listt[i]==listt[j]:
            rep+=1
    if rep>1:
        newLis.append(listt[i])
        print("repate number",listt[i],rep,"times")       

             
        