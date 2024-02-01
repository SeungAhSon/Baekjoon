import sys

# int => 36 : int_to_36(N)
# 36 => int : int(N, 36)
def int_to_36(N):
    quot, remain = divmod(N, 36)
    if quot == 0:  return d[remain]
    else:  return int_to_36(quot) + d[remain]

#count는 중요도를 나타내는 지표
d = list("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")
count = dict()
for i in d:  count[i] = 0

#orig_nums에 입력된 숫자의 값을 저장한다
orig_nums = []
N = int(sys.stdin.readline())
for _ in range(N):
  x = sys.stdin.readline().rstrip()
  orig_nums.append(x)
  for j in range(len(x)):  count[x[::-1][j]] += 36**j

#언급된 횟수에 Z와의 차이를 곱해준다
for i in d:  count[i] = count[i] * (35 - int(i, 36))
count = sorted(count.items(), key=lambda x: x[1], reverse=True)

#중요도가 큰 순서대로 K개를 Z 값으로 변경해준다
K = int(sys.stdin.readline())
for i in count[:K]:
  for j in range(N):
    orig_nums[j] = orig_nums[j].replace(i[0], "Z")

#합 계산
ans = 0
for j in range(N):  ans += int(orig_nums[j], 36)
print(int_to_36(ans))
