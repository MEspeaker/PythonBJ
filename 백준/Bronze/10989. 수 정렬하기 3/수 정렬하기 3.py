import sys
input=sys.stdin.readline
N=int(input().rstrip())
countList=[0]*10001
for _ in range(N):
    M=int(input().rstrip())
    countList[M]+=1
for j in range(len(countList)):
    for k in range(countList[j]):
        print(j)