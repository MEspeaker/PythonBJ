import sys

input=sys.stdin.readline
N,M=map(int,input().rstrip().split())
list=[(y+1) for y in range(N)]
for x in range(M):
  i,j=map(int,input().rstrip().split())
  list[i-1],list[j-1]=list[j-1],list[i-1]
print(*list)