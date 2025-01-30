import sys

input=sys.stdin.readline
digit="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sum=""
N,B=map(int,input().rstrip().split())
while N>0:
  M=N%B
  N=N//B
  sum+=digit[M]
sum=sum[::-1]
print(sum)