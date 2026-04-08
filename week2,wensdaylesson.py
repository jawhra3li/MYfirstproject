"""
###cubevolume fun
def cubeVolume(sidelength):
    if sidelength >=0:
        return sidelength**3
    else:
        return 0
#call fun    
cubevolume1=cubeVolume(-3)    
print(cubevolume1)  
cubevolume2=cubeVolume(2)    
print(cubevolume2)

###volume of pry with squae base
#compute the pry volume with squae base
#@parameter (heigth and length of base)
#@return to pry volume ((1/3)*H*L**2)
def pryvolume(L,H):
    if L and H >=0:
       return (1/3)*H*(L**2)
    else:
       return 0
    
#call function
result1=pryvolume(3,3)
print("the pyr volume with base area with 3Cm base length and 3Cm heigth is: ",result1)
result2=pryvolume(-1,-2)
print("the pyr volume with base area with -1Cm base length and -2 Cm heigth is: ",result2)

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
      
#check if the number is prime or not
#@parameter (i/p is number , check if <=1 not prime,check devision ability )
#@return to false or true


def isprime(n):
    if n<=1:
        return False
    i=2
    while i<n:
     if n%i==0:
        return False
     i+=1
    return True
##call
test1=isprime(78675)
print(test1)


#check if the number is perfect square or not
#@parameter (i/p is number , if squre is integer,it is perfect square
#@return to false or root
def square(n):
    root=n**0.5
    if root==int(root):
        return root
    else:
        return False
    
 ##call
result1=square(121)
print(result1)

##other sol
from math import *
def sqrrot(num):
    root=sqrt(num)
    if root.is_integer()==True:
        return root
    else:
        return False
    
print(sqrrot(9))

def boxstring(name):
 n=len(name)
 print(" - "*(n+4))
 print("!" +"         "+ name+"         !")
 print(" - "*(n+4))
boxstring("jouhara")

def readupto(high):
    v=int(input("enter value between o to "+str(high)+" : "))
    
def printtable(n):                              
    for i in range(1,13):
        print(n,"x",i,"=",n*i)
    return "end of print table for",n
 #call
num=int(input("enter you number"))
print(printtable(num))

###reseve
def reserveword(word):
    resev=word[::-1]
    return resev
print(reserveword("ali"))
    
##factorial
def factorial(n):
    result=1
    for i in range(1,(n+1)):
        result=result*i
    return result
##call
##num=int(input("enter your numer to find the fictorial"))
###print("the fictorial result for ",num,"is",factorial(num))
print(factorial(3))


def fibonacci(n):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(0,n):
       x=a+b
       print(x)
       a=b
       b=x
    return"-------end----------"
     
print(fibonacci(9))
"""
def sumsquare(n):
    sum=0
    for i in range(n+1):
        res=i*i
        sum+=res
    print("The squar root of",n,"is",res,"and sum is= ",sum)
    return"________end_______"
    
print(sumsquare(2))


def fibonacci(n):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(0,n):
       x=a+b
       print(x)
       a=b
       b=x
    return"-------end----------"
     
print(fibonacci(9))




    