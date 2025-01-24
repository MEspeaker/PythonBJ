import sys
input=sys.stdin.readline
list=['c=','c-','dz=','d-','lj','nj','s=','z=']
N=input().rstrip()
for i in range(len(list)):
  if list[i] in N:
    N=N.replace(list[i],'*')
print(len(N))