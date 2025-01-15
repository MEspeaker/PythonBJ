H,M=map(int,input().split())
temp=M-45
if(temp<0):
  if((H-1)<0):
    print(23, temp+60)
  else:
    print((H-1), (temp+60))
else:
  print(H, temp)