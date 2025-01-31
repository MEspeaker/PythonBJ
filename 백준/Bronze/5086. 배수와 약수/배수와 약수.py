import sys

input=sys.stdin.readline

while True:
  N,M=map(int,input().rstrip().split())
  if (N==0)&(M==0):
    break
  else:
    if N%M==0:
      print("multiple")
    else:
      if M%N==0:
        print("factor")
      else:
        print("neither")