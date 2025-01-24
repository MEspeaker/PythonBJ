import sys
input=sys.stdin.readline
N=int(input().rstrip())
count=N
for i in range(N):
  M=input().rstrip()
  for j in range(len(M)-1):
    if (M[j]!=M[j+1]) & (M[j] in M[j+1:]):
      count-=1
      break
print(count)