import sys

input=sys.stdin.readline
N=int(input().rstrip())
xlist=[]
ylist=[]
for i in range(N):
    x,y=map(int,input().rstrip().split())
    xlist.append(x)
    ylist.append(y)
maxX=max(xlist)
minX=min(xlist)
maxY=max(ylist)
minY=min(ylist)
print((maxX-minX)*(maxY-minY))