import sys
input=sys.stdin.readline
N=int(input().rstrip())
sugar=-1
if N%5==0:
    sugar=N//5
else:
    for i in range(N//5,-1,-1):
        if (N-5*i)%3==0:
            sugar=i+(N-5*i)//3
            break
print(sugar)