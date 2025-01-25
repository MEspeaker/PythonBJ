import sys
input=sys.stdin.readline
count=0
S=input().rstrip()
for i in range(0,len(S)-1):
  if S[i]!=S[i+1]:
    count=count+1
print((count+1)//2)
