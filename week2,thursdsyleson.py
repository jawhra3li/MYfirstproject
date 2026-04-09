"""
print(sumsquare(2))

fname="jaw ali"
finame=fname.split()[-1]
sname=fname.split()[0]


import re
text="SplitStrngByUpper"
result=re.split('(?=[A-Z])',text )
print(result)

width,lenth=map(int,input('enter width and length').split())
print(width)
print(lenth)

h,m=map(int,input('enter HH:MM').split(":"))
print(h)
print(m)

n,g=input('enter your name and gade').split()
print('your name is',n,'your age is',g)

b=1000
def withdraw(a):
    global b
    if b>=a:
        b-=a
withdraw(350)
print('balance',b)

v=lambda l:l**3
print(v(3))


num=lambda x : "+" if x>0 else "-" if x<0 else "0" 
print(num(0))

def fun(*args):
    for arg in args:
      print(arg)
fun(20,30)
fun(20,202,2)

def calclation(a,b):
    
 return a+b ,a-b
res=calclation(2,3)
print(res)
 
##by defult
def area(w,l=200):
    area1=w*l
    return area1

print(area(20))
print(area(20,30))

  
def fun(a,b):
    def fun2():
        return a+b
    return fun2()+5
print(fun(2,2))

def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
print(factorial(4))

def sumall(n):
    if n==0:
        return 0
    return n+sumall(n-1)
print(sumall(10))
"""
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return (fibonacci(n-1)+fibonacci(n-2))
print( fibonacci(3))

    
    
    
    
    
   
