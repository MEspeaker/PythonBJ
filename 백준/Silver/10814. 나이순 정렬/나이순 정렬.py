import sys
input=sys.stdin.readline
N=int(input().rstrip())
list=[]
for _ in range(N):
    x,y=map(str,input().rstrip().split())
    list.append([int(x),y])
list=sorted(list,key=lambda x:x[0])
for i in list:
    print(*i)