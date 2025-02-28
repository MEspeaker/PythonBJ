import sys
input=sys.stdin.readline
T=int(input().rstrip())
for _ in range(T):
    N=int(input().rstrip())
    P=[0]*(N+1)
    if(N<4):
        print(1)
        continue
    if(N==4):
        print(2)
        continue
    P[1]=1
    P[2]=1
    P[3]=1
    P[4]=2
    for i in range(5,N+1):
        P[i]=P[i-2]+P[i-3]
    print(P[N])