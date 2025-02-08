import sys
input=sys.stdin.readline
N=int(input().rstrip())
list=[]
for i in range(N):
    a,b,c,d=map(str,input().rstrip().split())
    list.append([a,int(b),int(c),int(d)])
list=sorted(list,key=lambda x:(-x[1],x[2],-x[3],x[0]))
for j in list:
    print(j[0])