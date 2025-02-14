import sys
input=sys.stdin.readline
N,C=map(int,input().rstrip().split())
house=[int(input().rstrip()) for _ in range(N)]
house.sort()
start,end=1,(house[-1]-house[0])
while start<=end:
    current=house[0]
    count=1
    mid=(start+end)//2
    for i in range(1,N):
        if (house[i]-current)>=mid:
            count+=1
            current=house[i]
    if count>=C:
        start=mid+1
    else:
        end=mid-1
print(end)