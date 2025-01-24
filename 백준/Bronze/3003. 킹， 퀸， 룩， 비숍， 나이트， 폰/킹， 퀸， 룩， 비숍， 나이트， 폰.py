import sys

input=sys.stdin.readline
list=[1,1,2,2,2,8]
N=[int(i) for i in input().rstrip().split()]
M=[list[x]-N[x] for x in range(len(list))]
print(*M)