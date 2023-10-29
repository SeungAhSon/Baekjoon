import sys

grade_dict = {'A+':4.5,'A0':4.0,'B+':3.5,'B0':3.0,'C+':2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F':0}

ans = 0
total_C = 0
for _ in range(20):
  S,C,G = sys.stdin.readline().rstrip().split(' ') #Subject, Credits, Grade
  if G=='P': pass
  else:
    C = float(C)
    G = grade_dict[G]
    total_C+=C
    ans+=C*G
  
print(ans/total_C)