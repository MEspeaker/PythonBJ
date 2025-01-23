import sys

input=sys.stdin.readline
T=int(input().rstrip())
for i in range(T):
  P=""
  R,S=map(str,input().rstrip().split())
  for j in S:
    for k in range(int(R)):
      P+=j
  print(P)