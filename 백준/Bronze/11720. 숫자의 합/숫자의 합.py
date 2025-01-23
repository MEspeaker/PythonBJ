import sys

input=sys.stdin.readline
sum=0
N=int(input().rstrip())
list=[int(i) for i in input().rstrip()]
for x in list:
  sum+=x
print(sum)