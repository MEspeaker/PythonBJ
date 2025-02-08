N=int(input())
mlist= list(map(int, input().split()))
mlist.sort()
print(mlist[(N-1)//2])