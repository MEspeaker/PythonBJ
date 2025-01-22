import sys

input=sys.stdin.readline
array1=[int(input().rstrip()) for _ in range(28)]
for i in range(1,31):
  if(array1.count(i)!=1):
    print(i)
