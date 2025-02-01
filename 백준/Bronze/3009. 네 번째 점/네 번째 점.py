import sys

input=sys.stdin.readline
xlist=[]
ylist=[]
for _ in range(3):
    x,y= map(int,input().rstrip().split())
    xlist.append(x)
    ylist.append(y)
for i in range(3):
    if xlist.count(xlist[i])!=2:
        print(xlist[i], end=" ")
        break
for i in range(3):
    if ylist.count(ylist[i])!=2:
        print(ylist[i])
        break
