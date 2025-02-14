import sys
input=sys.stdin.readline
N=int(input().rstrip())
A=[[int(input().rstrip()),i] for i in range(N)]
B=[j for j in A]
B.sort()
C=[]
for k in range(len(A)):
    C.append(B[k][1]-A[k][1])
print(max(C)+1)