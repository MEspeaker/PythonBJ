import sys
import string

input=sys.stdin.readline
list=[i for i in input().rstrip()]
for x in string.ascii_lowercase:
  if(list.count(x)!=0):
    for y in range(len(list)):
      if list[y]==x:
        print(y, end=" ")
        break
  else:
    print(-1, end=" ")