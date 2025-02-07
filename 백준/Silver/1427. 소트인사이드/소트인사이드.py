import sys
input=sys.stdin.readline
N=input().rstrip()
list=[int(i) for i in N]
list=reversed(sorted(list))
num=""
for j in list:
    num+=str(j)
print(num)