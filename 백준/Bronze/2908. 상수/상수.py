import sys

input=sys.stdin.readline
a,b= map(str,input().rstrip().split())
list1=[i for i in a]
list2=[j for j in b]
list1.reverse()
list2.reverse()
A="".join(list1)
B="".join(list2)
if int(A)>int(B):
  print(A)
else:
  print(B)
