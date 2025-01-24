import sys
import string
max=0
maxAlpah=""
count=0
countList=[]
input=sys.stdin.readline
N= input().rstrip()
for x in string.ascii_uppercase:
  count=N.upper().count(x)
  countList.append(count)
  if(count>max):
    max=count
    maxAlpah=x
if countList.count(max)==1:
  print(maxAlpah)
else:
  print("?")