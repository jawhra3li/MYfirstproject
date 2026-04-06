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