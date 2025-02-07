import sys
input=sys.stdin.readline
N=int(input().rstrip())
title=666
list=[]
while True:
    if len(list)==N:
        break
    if str(title).count("666")>=1:
        list.append(title)
    title+=1
print(list[N-1])