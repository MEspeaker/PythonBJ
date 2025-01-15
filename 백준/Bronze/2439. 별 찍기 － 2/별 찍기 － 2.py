N=int(input())
star=""
for i in range(1,N+1):
  sum=""
  for j in range(1,(N+1-i)):
    sum=sum+" "
  star=star+"*"
  sum=sum+star
  print(sum)