import sys
#브루트포스 방법으로 풀었다.

N = int(sys.stdin.readline()) # 희망 채널 번호
M = int(sys.stdin.readline()) #고장난 버튼의 개수
broken = list(sys.stdin.readline().rstrip().split())

# 현재 채널 100 기준으로 + 혹은 -만 사용
min_count = abs(100 - N)

for i in range(1000001):
  i = str(i)
  for j in range(len(i)):
    if i[j] in broken: break
    elif j==len(i)-1:   min_count = min(min_count, len(i)+abs(int(i)-N))
    
print(min_count)