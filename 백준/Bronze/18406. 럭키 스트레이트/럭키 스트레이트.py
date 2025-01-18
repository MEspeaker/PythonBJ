import sys
from collections import deque
dq= deque()
r=0
l=0
data=sys.stdin.readline().rstrip()
for i in data:
  dq.append(i)

while len(dq)!=0 :
  r=r+int(dq.pop())
  l=l+int(dq.popleft())

if(r==l):
  print("LUCKY")
else:
  print("READY")

