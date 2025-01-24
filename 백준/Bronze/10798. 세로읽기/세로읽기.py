import sys
input=sys.stdin.readline
list=[[i for i in input().rstrip()]for _ in range(5)]
max=0
for x in range(len(list)):
  y=len(list[x])
  if(y>max):
    max=y
matrix=[]
for p in range(max):
  for q in range(len(list)):
    if p < len(list[q]):
      print(list[q][p], end="")