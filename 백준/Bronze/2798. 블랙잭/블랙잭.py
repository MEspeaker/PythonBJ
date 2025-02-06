import sys

input=sys.stdin.readline
N,M=map(int,input().rstrip().split())
O=input().rstrip()
list=[int(i) for i in O.split()]
sumlist=[]
for j in range(N):
    for k in range(j+1,N):
        for l in range(k+1,N):
            sum=list[j]+list[k]+list[l]
            if sum<=M:
                sumlist.append(sum)
print(max(sumlist))