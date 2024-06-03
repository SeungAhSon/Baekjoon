def can_see(from_idx, to_idx):
  x1, y1 =  from_idx, buildings[from_idx]
  x2, y2 = to_idx, buildings[to_idx]
  slope = (y2 - y1) / (x2 - x1)
  intercept = y1 - slope * x1
  
  for i in range(x1 + 1, x2):
      y = slope * i + intercept
      if buildings[i] >= y:  return False
  return True

#=====input=====
N = int(input())
buildings = list(map(int, input().split()))

ans = 0
for i in range(N):
  temp = 0
  for j in range(N):
    if i<j and can_see(i,j): temp+=1
    elif j<i and can_see(j,i): temp+=1
  ans = max(ans, temp)

print(ans)
