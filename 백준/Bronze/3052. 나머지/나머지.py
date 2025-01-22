import sys

input=sys.stdin.readline
list=[int(input().rstrip())%42 for _ in range(10)]
setList=set(list)
print(len(setList))
