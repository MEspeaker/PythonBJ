import sys

input= sys.stdin.readline
N,X=map(int,input().rstrip().split())
A=input().rstrip()
list=[int(i) for i in A.split() if int(i)<X]
print(*list)
