import sys
input=sys.stdin.readline
N=int(input().rstrip())
list=[]
for i in range(N):
    x,y=map(int,input().rstrip().split())
    list.append((y,x))
list=sorted(list)
for i in list:
    print(*reversed(i))