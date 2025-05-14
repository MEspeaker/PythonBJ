import sys
from collections import deque
input=sys.stdin.readline

dr=[1,-1,0,0] #아래,위
dc=[0,0,1,-1] #오른쪽,왼쪽

n,k=map(int,input().rstrip().split())
matrix=[list(map(int, input().rstrip().split())) for _ in range(n)]
s,x,y=map(int,input().rstrip().split())

q=[]
for i in range(n):
  for j in range(n):
    if matrix[i][j]!=0:
      q.append((matrix[i][j],i,j,0)) #바이러스값,행,열,시간

q.sort()
q=deque(q)

while q:
  v,row,col,t=q.popleft()
  if t==s:
    continue
  for l in range(4):
    r= row+dr[l]
    c= col+dc[l]
    if 0<= r < n and 0<= c < n and matrix[r][c]==0:
      matrix[r][c]=v
      q.append((v,r,c,t+1))
print(matrix[x-1][y-1])