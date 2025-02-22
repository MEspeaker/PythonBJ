import sys
input=sys.stdin.readline
n=int(input().rstrip())
num=list(map(int,input().rstrip().split()))

def lis(arr):
    a=len(arr)
    dp=[1]*a
    for i in range(a):
        for j in range(i):
            if arr[j]<arr[i]:
                dp[i]=max(dp[i],dp[j]+1)
    return max(dp)

print(lis(num))