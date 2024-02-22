import sys

#55-50+40 = (55)-(50+40) = -35
#10+20+30+40 = (10+20+30+40) = 100
#00009-00009 = (00009)-(00009) = 0
#10-20-30-50 = (10)-(20)-(30)-(50) = -90
formula = sys.stdin.readline().rstrip()
formula_split = formula.split("-")

#맨 처음에 마이너스가 나올 경우 고려
ans = (-1 if formula[0]=='-' else 1) * sum(map(int,formula_split[0].split("+")))

for i in formula_split[1:]:
  ans-=sum(map(int,i.split("+")))

print(ans)