import sys
sys.setrecursionlimit(10 ** 6)
input=sys.stdin.readline
n,m,r=map(int,input().rstrip().split())
matrix=[[] for _ in range(n+1)]
isVisited=[False]*(n+1)
countList=[0]*(n+1)
count=0

def dfs(graph,v):
    global count
    isVisited[v]=True
    count+=1
    countList[v]=count
    for i in graph[v]:
        if not isVisited[i]:
            dfs(graph,i)

for j in range(m):
    u,v=map(int,input().rstrip().split())
    matrix[u].append(v)
    matrix[v].append(u)
for k in range(1,n+1):
    matrix[k].sort()

dfs(matrix,r)
for l in range(1,n+1):
    print(countList[l])