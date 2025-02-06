import sys
input=sys.stdin.readline
N,M=map(int,input().rstrip().split())
board=[input().rstrip() for _ in range(N)]
count=[]
for x in range(N-7):
    for y in range(M-7):
        index1 = 0 # W로 시작할경우
        index2 = 0 # B로 시작할경우
        for i in range(x, x+8):
            for j in range(y, y+8):
                if (i+j) % 2 == 0:
                    if board[i][j] != "W":
                        index1 += 1
                    if board[i][j] != "B":
                        index2 += 1
                else:
                    if board[i][j] != "B":
                        index1 += 1
                    if board[i][j] != "W":
                        index2 += 1
        count.append(min(index1, index2))
print(min(count))