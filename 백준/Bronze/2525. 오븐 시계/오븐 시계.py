H,M=map(int,input().split())
time=int(input())
temp=time+M
if(temp>=60):
  x=int(temp/60)
  y=temp%60
  if((H+x)>23):
    print((H+x-24), y)
  else:
    print(H+x,y)
else:
  print(H, temp)