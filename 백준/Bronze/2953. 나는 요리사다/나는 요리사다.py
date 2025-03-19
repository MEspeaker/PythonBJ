import sys
input=sys.stdin.readline
sumArray=[0]*5
for i in range(5):
  array=list(map(int,input().rstrip().split()))
  sumArray[i]=sum(array)
print(sumArray.index(max(sumArray))+1,max(sumArray))