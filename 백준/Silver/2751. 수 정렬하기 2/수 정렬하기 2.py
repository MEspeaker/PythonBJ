import sys
input=sys.stdin.readline
N=int(input().rstrip())
list=[int(input().rstrip()) for _ in range(N)]
list2=set(list)
list3=sorted(list2)
for i in list3:
    print(i)
