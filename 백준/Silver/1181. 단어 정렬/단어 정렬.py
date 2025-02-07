import sys
input=sys.stdin.readline
N=int(input().rstrip())
list=[input().rstrip() for _ in range(N)]
list2=set(list)
list3=[]
for i in list2:
    list3.append((len(i),i))
list3=sorted(list3)
for j in list3:
    print(j[1])