"""
counter=1
while counter <=10:
 print(counter,"loop",counter)
 counter+=1
 

years= 0 
balance=10000
while balance <20000:
     years+=1
     interest=balance*0.05
     balance=interest+balance
     print("years needed:",years,balance)    
   
     
counter=10
while counter >=0:
 print(counter,"loop",counter)
 counter-=1
 
print(counter) 
 
 ###if we do oppsite 
counter=10
while counter >=0:
 counter-=1   
 print(counter,"loop",counter)

#print all even n between 0-20

i=0
while i<=20:
     if i%2==0:
      print(i,"is even")
     else:
      print(i,"is odd")
     i+=1

i=0
while i<=20:
    i+=1
    if i%2==0:
      print(i,"is even")
    else:
      print(i,"is odd")
 
##prime
num=2
while num<=100:
  prime=True
  i=2
  while i<num:
    if num%i==0:
      prime=False
      break
    i+=1
  if prime:
      print(num)
  num+=1    
      
   ##anthor solution
 
num=2
while num<200:
 count=2
 isprime=True
 while count<num:
  if num%count==0:
   isprime=False
  count+=1
 
counter=0
sumb=0
while counter<=10:
    sumb+=counter
    counter+=1
    print("loop",counter,sumb)
print(sumb)

i=0
total=0
while total<10:
    i+=1
    total+=i
    print(i,total)
    
salary=0.0
total=0.0
count=0
while salary>=0:
 salary=float(input('input salary -1 to finish'))
 if salary>=0.0:
    total+=salary
    count+=1
    

#student grade averge 90/70/50/98
grade=0.0
count=0
total=0
while grade>=0:
 grade=float(input('enter your grade, if you want to stop enter -1'))
 if grade>=0:
  total+=grade
  count+=1
if count>0:
 avr=total/count
 print('the student avrage is=',avr)
else:
 print('unavalible')    

## max grade
max1=0
count=0
min1=100
while True:
    grade=input('enter your grade, if you want to stop enter end')
    if grade=="end":
        print('the program end')
        break
    count+=1
    grade=float(grade)
    if grade>=max1:
      max1=grade
    if grade<=min1:
     min1=grade
print('The max grade is: ',max1)    
print('The min grade is: ',min1) 

    
number=int(input('enter your number'))
count=0
while number !=' ':
  if number<0:
      count+=1
      print('the number of negitaves numers is: ',count)
      number=int(input('enter your number'))
  else:
     count-=1
     
inputstr=input('enter a value')
negc=0
while inputstr !=' ':
    val=int(inputstr)
    negc+=1
    inputstr=input('enter emty to end')
print(negc)
"""
      
      
   
 
 