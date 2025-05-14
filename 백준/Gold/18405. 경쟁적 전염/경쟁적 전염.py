import sys
from collections import deque
input = sys.stdin.readline

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

n, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())

q = []
for i in range(n):
    for j in range(n):
        if matrix[i][j] != 0:
            q.append((matrix[i][j], i, j, 0))  # (virus_type, row, col, time)

q.sort()  
q = deque(q)

while q:
    virus, r, c, time = q.popleft()
    if time == s:
        continue
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < n and 0 <= nc < n and matrix[nr][nc] == 0:
            matrix[nr][nc] = virus
            q.append((virus, nr, nc, time + 1))

print(matrix[x - 1][y - 1])
