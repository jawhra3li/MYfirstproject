n=int(input("enter number: "))
total=0
temp=n

while temp>0:
    digit=temp%10  ##last =9
    total=total+digit  ##add =9
    temp=temp//10 ##remove last
print("sum=",total)
