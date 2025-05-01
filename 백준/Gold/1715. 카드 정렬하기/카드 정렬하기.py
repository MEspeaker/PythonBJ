import sys
import heapq
input=sys.stdin.readline

N=int(input().rstrip())
num=[int(input().rstrip()) for _ in range(N)]
min_heap=[]
for n in num:
  heapq.heappush(min_heap,n)
total=0
while len(min_heap)>1:
  first=heapq.heappop(min_heap)
  second=heapq.heappop(min_heap)
  sum=first+second
  total+=sum
  heapq.heappush(min_heap,sum)
print(total)