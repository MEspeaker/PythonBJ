import sys
from bisect import bisect_left, bisect_right
input=sys.stdin.readline
N=int(input().rstrip())
mylist= list(map(int,input().rstrip().split()))
M=int(input().rstrip())
mylist2= list(map(int,input().rstrip().split()))
mylist.sort()
for i in mylist2:
    if bisect_left(mylist,i)>=len(mylist):
        print(0)
    else:
        if mylist[bisect_left(mylist,i)]==i:
            print(1)
        else:
            print(0)