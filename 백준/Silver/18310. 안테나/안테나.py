import sys
input=sys.stdin.readline
N=int(input().rstrip())
mylist= list(map(int, input().split()))
mylist=sorted(mylist)
print(mylist[(N-1)//2])