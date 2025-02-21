import sys
from collections import deque
input=sys.stdin.readline
n,m,k,x=map(int,input().rstrip().split()) #노드,간선,계층,시작
matrix=[[] for _ in range(n+1)]
isVisited=[False]*(n+1)
countList=[-1]*(n+1)
check=False

def bfs(graph,node):
    queue=deque([node])
    isVisited[node]=True
    countList[node]=0
    while queue:
        v=queue.popleft()
        for i in graph[v]:
            if not isVisited[i]:
                queue.append(i)
                isVisited[i]=True
                countList[i]=countList[v]+1
for j in range(m):
    u,v=map(int,input().rstrip().split())
    matrix[u].append(v)

bfs(matrix,x)
for l in range(1,n+1):
    if countList[l]==k:
        print(l)
        check=True
if not check:
    print(-1)
