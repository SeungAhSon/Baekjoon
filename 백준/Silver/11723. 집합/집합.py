import sys

M = int(sys.stdin.readline())
S = set()

# list의 append, remove 방식으로 쓰면 메모리 초과 (1 ≤ M ≤ 3,000,000)
# 집합을 구현한다는 점에서 set을 사용
# N의 범위가 1~20이라는 점을 고려하면 비트마스킹으로 구현하는 풀이도 있을 듯

for _ in range(M):
    command = sys.stdin.readline().strip().split()
    if len(command) == 1 : 
        if command[0] =="all" :
            S = set(i for i in range(1,21))
        else : S = set()
    else : 
        a,b = command[0], int(command[1])
        if a =="add" : S.add(b)
        elif a =="remove" : S.discard(b)
        elif a =="check" : print(1 if b in S else 0)
        elif a =="toggle" : S.discard(b) if b in S else S.add(b)