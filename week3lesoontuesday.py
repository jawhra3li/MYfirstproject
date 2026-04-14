"""
favcolor={"s":["red","yellow"],"f":"yellow","a":"pink"}

for key in favcolor:
    if type(favcolor[key]) is list:
        count=1
        for i in favcolor[key]:
            print(key,i,count)
            count=+1
    else:
     print(key,favcolor[key])
     
#list by user
mylist=list(input("enter your number list"))
repdic={}
for i in mylist:
    if i in repdic:
        repdic[i]+=1
    else:
        repdic[i]=1
print(repdic)

#my list
mylist=[1,2,4,6,1,3,3,3,4,7,8,9,9]
repdic={}
for i in mylist:
    if i in repdic:
        repdic[i]+=1
    else:
        repdic[i]=1

for values in repdic.values():
     print(values)
     
for key in repdic.keys():
     print(key)
 
a=((1,2,1),(3,34,5))
for i in a:
    for j in i:
        print(j,end="")
    print()
c=(1,2,2,1,2,1)
b=c.count(1)
print(b)
newset=set()
newset={1,1,1,12,23,3,4,5,6,7}
print(newset)
print(type(newset))
listt=[1,5,6,7,6]
e=set(listt)
listt2=[1,[5,6],7,6]
e2=set(listt)

"""
records = [
    ("Ali", "Math", 85),
    ("Sara", "Math", 90),
    ("Ali", "Science", 78),
    ("Sara", "Science", 88),
    ("Ali", "English", 92),
    ("Sara", "Englis",85)
    ]
result={}
for name, subject, mark in records:
    if name not in result:
        result[name] = {}
    result[name][subject] = mark

student_avg = {}
for name in result:
    total = sum(result[name].values())
    count = len(result[name])
    student_avg[name] = total / count

print("Average per student:")
print(student_avg)

subject_total = {}
subject_count = {}

for name in result:
    for subject in result[name]:
        mark = result[name][subject]
        subject_total[subject] = subject_total.get(subject, 0) + mark
        subject_count[subject] = subject_count.get(subject, 0) + 1

subject_avg = {}
for subject in subject_total:
    subject_avg[subject] = subject_total[subject] / subject_count[subject]
print("Average per subject:")
print(subject_avg)






    
    
    
     