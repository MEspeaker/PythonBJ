import sys

input=sys.stdin.readline
N=int(input().rstrip())
M=input().rstrip()
numbers=[i for i in M.split()]
isPrime=[True for _ in range(N)]
for j in range(N):
    if int(numbers[j]) < 2:  
        isPrime[j] = False
    else:
        for k in range(2, int(int(numbers[j])**0.5) + 1):
            if int(numbers[j]) % k == 0:
                isPrime[j] = False
                break  

list2 = [numbers[m] for m in range(N) if isPrime[m]]
print(len(list2))