"""
#new sol
lis=[3,3,4,5,7,3,4,3]
chec=[]
for i in lis:
    rep=0
    if lis not in chec:
     for j in lis:
        if i==j:
            rep+=1
     chec.append(lis)
     if rep>1:
        print(i,"repated",rep,"time")

friend=["wajed","jaw","reem","malak"]
friend.insert(1,"galia")

#usingg loop
friend=["wajed","jaw","reem","malak"]
friend.append("")
x=1
###n=str(input("enter new friend"))
###p=int(input("enter the postion)
for i in range(len(friend),1,-1):
    friend[i]=friend[i-1]
friend[x]="ali"    
print(friend)

friend=["wajed","jaw","reem","malak"]
friend.insert(1,"galia")
print(friend)
if "ali"not in friend:
    print("not found")
if "jaw"in friend:
    print("founded")
n=friend.index("jaw")
print(n)
friend.pop()
print(friend)
friend.remove("jaw")
print(friend)
friend.pop(2)
print(friend)
### friend.remove("ali")
print(friend)
list1=[1,1,12]
list2=[5,5,54]
listall=list1+list2
print(listall)
rep=list1*4
print(rep)

def mullis(lis,factor):
    lis=list(lis)
    for i in range (len(lis)):
        lis[i]=lis[i]*factor
    print(lis)   ##ref by value   
    return lis
listt=[1,1,4,5,7,9]
factor=4
mullis(listt,4)
print(listt)
listt2=[1,1,4,5,6,9,55,9]
slicingtest=listt[1:3]
print(slicingtest)
listt2[2:5]=[4,4,4]

values=[1,56,78,90]
limit=56
p=0
found=False
while p<len(values) and not found:
    if values[p]>limit:
        found=True
    else:
        p+=1
if found :
    print('found at',p)
else:
    print('not found')

a=[
    [1,2,1],
    [2,5,3],
    [5,8,9]
    ]
print(a)

b=[1,2,1]
c=[2,5,3]
d=["a","4","d"]

for i in range(4):
    if i==1:
        print(b)
    else:
        if i==2:
            print(c)
        else:
            if i==3:
                print(d)
                
a=[
    [1,2,1],
    [2,5,3],
    [5,8,9]
    ]                
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j]," ",end="")
    print()
   
data=[
    [2,4,5,1],
    [3,2,9,6],
    [1,0,2,10],
    ]
summ=[]
for i in range(len(data)):
    total=sum(data[i])
    summ.append(total)
    print(summ)
for j in range(len(data[i])):
     print (data[i])
maxx=max(summ)
maxxi=summ.index(maxx)
print("highest sum",maxx)
print("row index with hight sum:",maxxi)

data=[
    [2,4,5,1],
    [3,2,9,6],
    [1,0,2,10]
    ]
print(data)
"""
favcolor={"s":["red","yellow"],"f":"yellow","a":"pink"}

sfav=favcolor["s"]
###print(favcolor.get("s","not found")
favcolor["s"]="blue"

