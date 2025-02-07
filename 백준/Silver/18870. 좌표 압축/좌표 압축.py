import sys
input=sys.stdin.readline
N=int(input().rstrip())
M=input().rstrip()
list=[int(i) for i in M.split()]
list2=set(list)
list3=sorted(list2)
dic={list3[j]: j for j in range(len(list3))}
for k in list:
    print(dic[k],end=" ")