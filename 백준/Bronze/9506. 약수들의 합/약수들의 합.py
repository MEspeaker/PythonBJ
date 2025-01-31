import sys

input=sys.stdin.readline
while True:
  sum=0
  N=int(input().rstrip())
  if N==-1:
    break
  else:
    list=[i for i in range(1,N) if N%i==0]
    for j in list:
      sum+=j
    list2=[]
    list2.append(str(N))
    if(sum==N):
      list2.append("=")
      for k in list:
        list2.append(str(k))
        list2.append("+")
      list2.pop()
      print(*list2)
    else:
      print(*list2,"is NOT perfect.")
