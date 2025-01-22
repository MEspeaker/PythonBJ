import sys

input=sys.stdin.readline
N,M=map(int,input().rstrip().split())
list=[0 for _ in range(N)]
for x in range(M):
  i,j,k=map(int,input().rstrip().split())
  for y in range(i-1,j):
    list[y]=k
print(*list)
