import sys

input= sys.stdin.readline
N=input().rstrip()
M=input().rstrip()
list=[int(i) for i in M.split()]
print(min(list), max(list))