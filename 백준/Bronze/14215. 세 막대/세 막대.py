import sys

input=sys.stdin.readline
a,b,c=map(int,input().rstrip().split())
a,b,c=sorted([a,b,c])
if a+b<=c:
    c=a+b-1
print(a+b+c)