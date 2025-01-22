import sys

input=sys.stdin.readline
N=input().rstrip()
M=input().rstrip()
sum=0
list=[int(i) for i in M.split()]
list2=[(j/max(list))*100 for j in list]
for x in list2:
  sum=sum+x
print(sum/len(list2))
