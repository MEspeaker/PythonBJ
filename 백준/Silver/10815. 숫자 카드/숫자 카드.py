import sys
input=sys.stdin.readline
N=int(input().rstrip())
a=list(map(int,input().rstrip().split()))
M=int(input().rstrip())
b=list(map(int,input().rstrip().split()))
data=dict()
for i in a:
  data[i]=0
for j in b:
  if j in data:
    print(1, end=" ")
  else:
    print(0, end=" ")