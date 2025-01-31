import sys

input=sys.stdin.readline
N,K=map(int,input().rstrip().split())
list=[i for i in range(1,N+1) if N%i==0]
if K>len(list):
  print(0)
else:
  print(list[K-1])