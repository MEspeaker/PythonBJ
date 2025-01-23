import sys

input=sys.stdin.readline
T=int(input().rstrip())
for y in range(T):
  S=[x for x in input().rstrip()]
  print(S[0],S[len(S)-1],sep="")