import sys
input=sys.stdin.readline
matrix=[list(map(int,input().rstrip().split()))for _ in range(9)]
max=0
xPos=0
yPos=0
for x in range(len(matrix)):
  for y in range(len(matrix[x])):
    if matrix[x][y]>max:
      xPos=x
      yPos=y
      max=matrix[x][y]
print(max)
print(xPos+1, yPos+1)