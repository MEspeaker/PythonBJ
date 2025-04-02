import sys
from collections import deque

input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    isError = False
    p = input().strip()
    n = int(input().strip())
    x = input().strip()
    flag=0
    if n == 0:
        dq = deque()
    else:
        dq = deque(map(int, x[1:-1].split(',')))

    for cmd in p:
        if cmd=='R':
            flag+=1
        elif cmd == 'D':
            if dq:
                if flag%2==0:
                    dq.popleft()  
                else:
                    dq.pop()  
            else:
                isError = True
                break
    if isError:
        print("error")
    else:
        if flag%2!=0:
            dq.reverse()  
        print("[" + ",".join(map(str, dq)) + "]")
