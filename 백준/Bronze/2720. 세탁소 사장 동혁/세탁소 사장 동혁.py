import sys

input=sys.stdin.readline
list=[25, 10, 5, 1]
T=int(input().rstrip())
for i in range(T):
  N=int(input().rstrip())
  sum=""
  for j in list:
    M=str(N//j)
    sum=sum+ M+ " "
    N=N%j
  print(sum)