import sys

input=sys.stdin.readline
num=1
N=int(input().rstrip())
M=1
if(N==1):
  print(1)
else:
  while M<N:
    M=M+6*num
    num=num+1
  print(num)