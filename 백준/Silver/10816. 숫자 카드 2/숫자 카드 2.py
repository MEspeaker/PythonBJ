import sys
from bisect import bisect_left,bisect_right
input=sys.stdin.readline
N=int(input().rstrip())
mylist= list(map(int,input().rstrip().split()))
M=int(input().rstrip())
mylist2= list(map(int,input().rstrip().split()))
mylist.sort()
for i in mylist2:
    print(bisect_right(mylist,i)-bisect_left(mylist,i), end=" ")