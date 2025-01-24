import sys
input=sys.stdin.readline
N,M=map(int,input().rstrip().split())
matrixA=[list(map(int,input().rstrip().split()))for _ in range(N)]
matrixB=[list(map(int,input().rstrip().split()))for _ in range(N)]
matrixC=[[matrixA[i][j]+matrixB[i][j] for j in range(M)]for i in range(N)]
for x in matrixC:
  print(*x)