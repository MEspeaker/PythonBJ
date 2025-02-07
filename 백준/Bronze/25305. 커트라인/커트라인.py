import sys
input=sys.stdin.readline
N,k=map(int,input().rstrip().split())
grade=input().rstrip()
list=[int(i) for i in grade.split()]
list2=sorted(list)
print(list2[len(list2)-k])