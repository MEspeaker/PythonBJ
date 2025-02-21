import sys
from collections import deque
input=sys.stdin.readline
n,m,r=map(int,input().rstrip().split())
matrix=[[]for _ in range(n+1)]
isVisted=[False]*(n+1)
countList=[0]*(n+1)
count=0

def bfs(graph,node):
    global count
    queue=deque([node])
    isVisted[node]=True
    countList[node]=1
    while queue:
        v= queue.popleft()
        count+=1
        countList[v]=count
        for i in graph[v]:
            if not isVisted[i]:
                queue.append(i)
                isVisted[i]=True
                

for _ in range(m):
    u,v=map(int,input().rstrip().split())
    matrix[u].append(v)
    matrix[v].append(u)
for j in range(1,n+1):
    matrix[j].sort()

bfs(matrix,r)
for k in range (1,n+1):
    print(countList[k])