N = int(input())
nums = list(map(int, input().split()))
nums = sorted(nums)

print(nums[N//2])