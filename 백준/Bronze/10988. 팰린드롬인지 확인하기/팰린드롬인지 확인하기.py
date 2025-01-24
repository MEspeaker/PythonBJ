import sys

input=sys.stdin.readline
list=[i for i in input().rstrip()]
if len(list)%2==0:
  list1=[list[x] for x in range(len(list)//2)]
  list2=[list[y] for y in range(len(list)//2,len(list))]
  list2.reverse()
else:
  list1=[list[x] for x in range(len(list)//2)]
  list2=[list[y] for y in range(len(list)//2+1,len(list))]
  list2.reverse()
if(list1==list2):
  print(1)
else:
  print(0)