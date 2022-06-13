#N,M의 입력범위가 100,000을 넘어가면 시간 복잡도는 O(NM)이 되므로 1초 이내에 구현이 불가능하다.
#따라서 입력마다 계산하기보다는
#미리 정보를 저장해놓고 불러오는 식으로 접근하면 시간이 훨씬 줄어들게 된다.

import sys

N,M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

total = [0]
for i in range(N):
    total.append(total[i]+num[i])
    
for _ in range(M):
    A,B = map(int, sys.stdin.readline().split())
    print(total[B]-total[A-1])
