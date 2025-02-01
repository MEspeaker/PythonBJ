import sys

input=sys.stdin.readline
N=int(input().rstrip())
M=int(input().rstrip())
numbers=[i for i in range(N,M+1)]
isPrime=[True for _ in range(M-N+1)]
for j in range(M-N+1):
    if int(numbers[j]) < 2:  
        isPrime[j] = False
    else:
        for k in range(2, int(int(numbers[j])**0.5) + 1):
            if int(numbers[j]) % k == 0:
                isPrime[j] = False
                break  

list2 = [numbers[m] for m in range(M-N+1) if isPrime[m]]
if(len(list2)>0):
    sum=0
    for x in list2:
        sum+=x
    print(sum)
    print(min(list2))
else:
    print(-1)