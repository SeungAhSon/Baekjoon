import sys
min, max = map(int, sys.stdin.readline().split())

answer = max-min+1
TF = [0] *answer

for i in range(2, int(max**0.5+1)):
  for j in range((((min-1)//i**2)+1)*(i**2), max+1, i**2):
    if not TF[j-min] :
      TF[j-min] = 1
      answer -= 1
print(answer)