x=int(input())
y=input()
a=[]
for i in y:
  a.append(i)
a.reverse()
for j in a:
  print(int(j)*x)
print(x*int(y))