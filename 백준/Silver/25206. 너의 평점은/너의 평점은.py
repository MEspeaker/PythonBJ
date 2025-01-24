import sys
input=sys.stdin.readline
dict={'A+':4.5, 'A0': 4.0,'B+':3.5,'B0':3.0,'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}
sum=0
scoreSum=0
for i in range(20):
  subject,score,grade=map(str,input().rstrip().split())
  if(grade!='P'):
    scoreSum+=float(score)
    sum+=float(score)*dict[grade]
print(sum/scoreSum)
