import sys

input=sys.stdin.readline
x,y,w,h=map(int,input().rstrip().split())
list=[]
list.append(w-x)
list.append(h-y)
list.append(x)
list.append(y)
print(min(list))
