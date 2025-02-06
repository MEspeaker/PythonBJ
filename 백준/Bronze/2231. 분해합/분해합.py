import sys

input=sys.stdin.readline
N=int(input().rstrip())
check=False
for x in range(max(0,N-len(str(N))*9),N):
    sum=0
    for y in str(x):
        sum+= int(y)
    if (x+sum)==N:
        check=True
        print(x)
        break
if check==False:
    print(0)