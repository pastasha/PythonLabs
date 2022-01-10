import math

def fact(f):
    s=1
    for temp in range(2,f+1):
        s=s*temp
    return s

try:
    x=int(input('x= '))
    n=int(input('n= '))
    s=0;
    for i in range(1,n+1):
        temp=(x**i)*math.log(i)*5/fact(i)
        s+=temp
    y=s
    print(y)
except ValueError:
    print(e)
