import sys
input=sys.stdin.readline

def lis(arr):
  dp=[1]*n
  for i in range(len(arr)):
    for j in range(i):
      if arr[i]<arr[j]:
        dp[i]=max(dp[i],dp[j]+1)
  return max(dp)
n=int(input().rstrip())
w=list(map(int,input().rstrip().split()))
print(n-lis(w))