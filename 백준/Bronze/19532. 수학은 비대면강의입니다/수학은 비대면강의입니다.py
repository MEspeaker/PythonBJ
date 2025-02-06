import sys
input=sys.stdin.readline
a,b,c,d,e,f=map(int,input().rstrip().split())
print((c*e-b*f)//(a*e-b*d),(c*d-a*f)//(d*b-a*e))