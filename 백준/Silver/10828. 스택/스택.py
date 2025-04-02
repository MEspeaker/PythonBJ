import sys
input=sys.stdin.readline
stack=[]
N=int(input().rstrip())
for _ in range(N):
  M=input().rstrip()
  if("push" in M):
    stack.append(int(M[5:]))
  elif("pop" in M):
    if(len(stack)!=0):
      print(stack.pop())
    else:
      print(-1)
  elif(M=="size"):
    print(len(stack))
  elif(M=="empty"):
    if(len(stack)!=0):
      print(0)
    else:
      print(1)
  elif("top" in M):
    if(len(stack)!=0):
      print(stack[-1])
    else:
      print(-1)