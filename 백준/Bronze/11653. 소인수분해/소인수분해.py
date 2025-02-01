import sys

input=sys.stdin.readline
N=int(input().rstrip())
if(N!=1):
    for _ in range(N):
        for i in range(2,N+1):
            if N%i==0:
                print(i)
                N=N//i
                break