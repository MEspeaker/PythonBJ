import sys

input=sys.stdin.readline
N=int(input().rstrip())
print(((N-2)*(N-1)*(2*N-3)+3*(N-1)*(N-2))//12)
print(3)