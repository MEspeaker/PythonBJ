import sys

input=sys.stdin.readline
N,M=map(int,input().rstrip().split())
list=[x+1 for x in range(N)]
for y in range(M):
  i,j=map(int,input().rstrip().split())
  while i<j:
    list[i-1],list[j-1]=list[j-1],list[i-1]
    i=i+1
    j=j-1
print(*list)