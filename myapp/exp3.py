from myPackage.myModule import *
from math import factorial
print(factorial(5))
def sin(a,b):
    sine = 0
    for i in range(n):
        sign = (-1)**i
        pi=22/7
        y=x*(pi/180)
        sine += (MyMath.power(y,2.0*i+1)/MyMath.fact(2*i+1))*sign
    return sine
def cosine(x,n):
    cosx = 1
    sign = -1
    for i in range(2, n, 2):
        pi=22/7
        y=x*(pi/180)
        cosx = cosx + (sign*MyMath.power(y,i))/MyMath.fact(i)
        sign = -sign
    return cosx
x=int(input("Enter the value of x in degrees:"))
n=int(input("Enter the number of terms:"))
print('sine value is ')
print(round(sin(x,n),2))
print('cosine value is ')
print(round(cosine(x,n),2))
if(round(sin(x,n)))==1.0 :
    print('tan value is undefined')
else :
    print('tan value is ')
    print(round(sin(x,n)/cosine(x,n),2))






