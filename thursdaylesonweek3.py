"""
file.close()
file=open("C:/Users/DELL/Desktop/Jouhara/test.txt","r")
text=file.read()
wordlist=text.split()
print("the wod:",wordlist)
print("the number of word",len(wordlist))
for i in range(len(wordlist)):
               wordlist[i]=wordlist[i].lower().strip()
               if wordlist[i].lower().strip()=="the":
                 countt=wordlist.count(wordlist[i].lower().strip())
                 
print("num of the in text",countt)
#________________________________________________________________________
listt=[]
for index in range(len(listt)):
    if index==(len(listt))-1:
        print(wordlist[listt[index]: ])
    else:
        print(wordlist[listt[index]:wordlist[listt[index+1]]])

file.close()


###

amount=200
balance=100
if amount>balance:
    raise ValueError("amount ...")


try:
    filee=open("C:/Users/DELL/Desktop/Jouhara/test.txt","w")
    linee=filee.readline()
    print(linee)
    print(5/0)
    
except IOError:
    print("could not found")
except Exception as exceptObj:
    print("Error:",str(exceptObj))
finally:filee.close()
"""
inputu=False
while(inputu==False):
    try:
        num=input("enter num:")
        num=float(num)
        inputu=True
    except ValueError:
        print("can not convert '%s' "%num)
num=num*2
print(num)
    
