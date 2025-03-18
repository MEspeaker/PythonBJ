import sys
input=sys.stdin.readline
N=int(input().rstrip())
for _ in range(N):
  score=0
  scoreSum=0
  M=input().rstrip()
  for i in range(0,len(M)):
    if M[i]=="X":
      score=0
    else:
      score=score+1
    scoreSum+=score
  print(scoreSum)