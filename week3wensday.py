dic1 = {
    "Sunday": [30,29],
    "Monday": [29,31],
    "Tuesday": [31,30],
    "Wednesday": [33,32],
    "Thursday": [35,33],
    "Friday": [28,30],
    "saturday": [25,23],
    
    }

"""t=0
for day,tem in dic1.items():
    #print(day,tem)
#first week
    print(day,tem[0])   

##averge using key
for key in dic1:
    t=t+dic1[key][1]
av=t/len(dic1)
print(av)

##average uing items
for day,tem in dic1.items():
    t=t+tem[1]
av=t/len(dic1)
print(av)

list1=list(dic1)
print(list1)


for day in dic1:
    temp3=int(input("enter third week tem"))
    dic1[day].append(temp3)
print(dic1)
##new task 
result=(dic1.items())
for day in result:
    temp4=int(input("enter forth week tem"))
result=list(dic1.items())    
result.insert(3,temp4)
print(result)
##
lis=[1,1,12,3,4,4,4]
i=0
for key in dic1.keys():
    dic1[key].append(lis[i])
    i+=1
print(dic1)
"""    
print((dic1)+(dic1)
dic1.add(dic1)