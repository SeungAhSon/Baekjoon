import sys

def Dynamic(dp, nums):
    dp[0] = nums[0]
    for i in range(1, len(nums)):
        dp[i] = max(dp[i-1]+nums[i], nums[i])
    return max(dp)

N = int(sys.stdin.readline())
temp_list = list(map(int, sys.stdin.readline().split()))

dp = [0]*N
print(Dynamic(dp, temp_list))