import sys

input=sys.stdin.readline
a=int(input().rstrip())
b=int(input().rstrip())
c=int(input().rstrip())
if(a+b+c==180):
    if(a==b)&(b==c):
        print("Equilateral")
    else:
        if(a==b):
            print("Isosceles")
        elif(b==c):
            print("Isosceles")
        elif(a==c):
            print("Isosceles")
        else:
            print("Scalene")
else:
     print("Error")