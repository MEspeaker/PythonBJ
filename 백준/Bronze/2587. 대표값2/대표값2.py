import sys
input=sys.stdin.readline
list=[int(input().rstrip()) for _ in range(5)]
list2=sorted(list)
sum=0
for i in list2:
    sum+=i
print(sum//5)
print(list2[2])