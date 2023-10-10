import sys

N, C = map(int, sys.stdin.readline().split())
sequence = list(map(int, sys.stdin.readline().split()))

frequency = {}
order = 1 #입력이 된 순서
for num in sequence:
    if num in frequency:  frequency[num][0] += 1
    else:  
      frequency[num] = [1,order]
      order+=1

sorted_temp = sorted(frequency.keys(), key=lambda k: (-frequency[k][0], frequency[k][1]))

ans = []
for i in sorted_temp:  ans+=[i]*frequency[i][0]
print(*ans)