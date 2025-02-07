import sys
input=sys.stdin.readline
N=int(input().rstrip())
list=[int(input().rstrip()) for _ in range(N)]
list2=sorted(list)
for i in list2:
    print(i)