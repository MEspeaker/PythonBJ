import sys
input=sys.stdin.readline
N=int(input().rstrip())
whiteRec=[[0 for _ in range(100)]for _ in range(100)]
for _ in range(N):
    x, y = map(int, input().rstrip().split())
    for i in range(y, y + 10):
        for j in range(x, x + 10):
            whiteRec[i][j] = 1 
sum=0
for i in range(len(whiteRec)):
  sum+=whiteRec[i].count(1)

print(sum)
