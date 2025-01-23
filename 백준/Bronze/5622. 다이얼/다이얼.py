import sys

input=sys.stdin.readline
sum=0
num=['0','1','ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
list=[i for i in input().rstrip()]
for j in list:
  for k in range(len(num)):
    if j in num[k]:
      sum+=(k+1)
print(sum)