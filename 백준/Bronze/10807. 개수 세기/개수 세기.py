import sys

input= sys.stdin.readline
N=int(input().rstrip())
M=input().rstrip()
v=int(input().rstrip())
array=[int(i) for i in M.split() if int(i)==v]
print(len(array))