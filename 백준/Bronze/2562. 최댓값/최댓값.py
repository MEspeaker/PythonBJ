import sys

input= sys.stdin.readline
index=1
list=[int(input().rstrip()) for _ in range(9)]
print(max(list))
for i in list:
  if i==max(list):
    print(index)
    break
  index=index+1

