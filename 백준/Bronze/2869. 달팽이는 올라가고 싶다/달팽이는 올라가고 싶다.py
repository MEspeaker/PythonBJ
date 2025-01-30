import sys

input=sys.stdin.readline
A,B,V=map(int,input().rstrip().split())
if V<=A:
  print(1)
else:
  day=(V-A)//(A-B)
  if (V-A)%(A-B)!=0:
    day=day+1
  print(day+1)