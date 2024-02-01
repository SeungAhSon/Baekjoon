T = int(input())
for tc in range(1,T+1):
  N = int(input())
  nums = list(map(int, input().split()))
  ans = 0
  
  current_max = 0
  for i in range(N-1, -1,-1):
    if nums[i]>=current_max: current_max = nums[i]
    else : ans +=current_max-nums[i]

  print("#{} {}".format(tc, ans))