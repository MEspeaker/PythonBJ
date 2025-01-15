T=int(input())
array=[]
for i in range(1,T+1):
  A,B=map(int,input().split())
  array.append(A+B)
for j in array:
  print(j)