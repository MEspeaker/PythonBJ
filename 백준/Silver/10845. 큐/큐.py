import sys
import queue
input=sys.stdin.readline
q=queue.Queue()
N=int(input().rstrip())
for _ in range(N):
  M=input().rstrip()
  if("push" in M):
    q.put(int(M[5:]))
  elif("pop" in M):
    if(q.qsize()!=0):
      print(q.get())
    else:
      print(-1)
  elif(M=="size"):
    print(q.qsize())
  elif(M=="empty"):
    if(q.qsize()!=0):
      print(0)
    else:
      print(1)
  elif(M=="front"):
    if(q.qsize()!=0):
      print(q.queue[0])
    else:
      print(-1)
  elif(M=="back"):
    if(q.qsize()!=0):
      print(q.queue[-1])
    else:
      print(-1)