import sys
input=sys.stdin.readline
n=int(input().rstrip())
m=int(input().rstrip())
INF=float('inf')
graph=[[INF]*(n+1)for _ in range(n+1)]

for _ in range(m):
  s,d,w=map(int,input().rstrip().split())
  if graph[s][d]>= w:
    graph[s][d]=w

for k in range(1,n+1):
  graph[k][k]=0
  for i in range(1,n+1):
    for j in range(1,n+1):
      graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])
  

for i in range(1,n+1):
  for j in range(1,n+1):
    if graph[i][j]==INF:
      graph[i][j]=0
    print(graph[i][j], end=' ')
  print()