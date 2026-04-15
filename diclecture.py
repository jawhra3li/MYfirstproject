dic={
    "sunday":30,
    "monday":29,
    "tuseday":31,
    "wensday":33,
    "thursday":35,
    "friday":28,
    "saturaday":25,
    
    }
total=0
for key in dic:
    total+=dic[key]
    
#find average 2 method
av=total/len(dic)
summ=sum(dic.values())/len(dic)
#max
maxx=max(dic.values())
maxxx=0
for value in dic.values():
    if value>maxxx:
        maxxx=value
#MIN
minn=min(dic.values())
minnn=100
for value in dic.values():
    if value<minnn:
        minnn=value
#loop items find max
for item in dic.items():
    print(item[0],item[1])  #as tuple returning
    if item[1]==maxx:
        print("the highest temp is on ",item[0])
#loop items find min
for item in dic.items():
    print(item[0],item[1])  #as tuple returning
    if item[1]==minn:
        print("the lowest temp is on ",item[0])
        
for day,tem in dic.items():
    if item[1]==maxx:
        print(day)
        
                    
        
        
"""        
#find length
print(len(dic))
print(dic["wensday"])
lastweek=[]
for key in dic:
    print(key,dic[key])
    lastweek.append((key,dic[key]))
"""    
    
    
    
    
    
    

