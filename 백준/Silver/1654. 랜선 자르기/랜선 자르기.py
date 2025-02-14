import sys
input=sys.stdin.readline
K,N=map(int,input().rstrip().split())
list=[int(input().rstrip()) for _ in range(K)]
start,end=1,max(list)
while start<=end:
    mid=(start+end)//2
    total=0
    for i in list:
        count=i//mid
        total+=count
    if total>=N:
        start=mid+1
    else:
        end=mid-1
print(end)