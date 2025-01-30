import sys

input=sys.stdin.readline
sum=0
N,B=map(str,input().rstrip().split())
if(int(B)>10):
  for i in range(len(N)):
    if N[i].isdigit():
      sum+=(int(B)**(len(N)-(i+1)))*int(N[i])
    else:
      sum+=(int(B)**(len(N)-(i+1)))*(ord(N[i])-55)
  print(sum)
elif(int(B)<10):
  for i in range(len(N)):
    sum+=(int(B)**(len(N)-(i+1)))*int(N[i])
  print(sum)
else:
  print(int(N))