import sys

input=sys.stdin.readline
while True:
    a,b,c=map(int,input().rstrip().split())
    if(a==0&b==0&c==0):
        break
    if a>=b:
        if a>=c: #가장긴변a
            if b+c>a:
                if (a==b)&(b==c):
                    print("Equilateral")
                elif (a==b):
                    print("Isosceles")
                elif (b==c):
                    print("Isosceles")
                elif(a==c):
                    print("Isosceles")
                else:
                    print("Scalene")
            else:
                print("Invalid")
        else: #가장긴변c
            if a+b>c:
                if (a==b):
                    print("Isosceles")
                elif (b==c):
                    print("Isosceles")
                else:
                    print("Scalene")
            else:
                print("Invalid")
    else: #a<b
        if b>=c: #가장긴변b
            if a+c>b:
                if (b==c):
                    print("Isosceles")
                elif (a==c):
                    print("Isosceles")
                else:
                    print("Scalene")
            else:
                print("Invalid")
        else: #가장긴변c a<b<c
            if a+b>c:
                print("Scalene")
            else:
                print("Invalid")
