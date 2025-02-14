import sys
input=sys.stdin.readline
N,M=map(int,input().rstrip().split())
tree=list(map(int,input().rstrip().split()))
start,end=0,max(tree)
while start<=end:
    total=0
    mid=(start+end)//2
    for i in tree:
        if i>mid:
            total+=(i-mid)
        if total>M:
            break
    if total>=M:
        start=mid+1
    else:
        end=mid-1
print(end)