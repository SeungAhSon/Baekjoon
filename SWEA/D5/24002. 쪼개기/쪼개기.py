from collections import deque

#import sys
#sys.stdin = open("input.txt", "r")

def get_possible_lengths(x):
    visited = {}
    queue = deque()
    queue.append((x,0))
    
    while queue:
        curr, cost = queue.popleft()
        if curr in visited : continue
        visited[curr] = cost
        
        if curr>=2:
            half = curr // 2
            rest = curr - half
            queue.append((half, cost + 1))
            queue.append((rest, cost + 1))
    return visited

def solve_case(arr):
    all_possible_answers = [get_possible_lengths(x) for x in arr]
    #print('all_possible_answers', all_possible_answers)

    common_lengths = set(all_possible_answers[0].keys())
    #print('common_lengths',common_lengths)

    for dic in all_possible_answers[1:]:
        common_lengths &= set(dic.keys())
    
    min_ops = float('inf')
    for length in common_lengths:
        total_ops = sum(dic[length] for dic in all_possible_answers)
        min_ops= min(min_ops, total_ops)
    return min_ops

 
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    arr = list(map(int, input().split()))
    print(solve_case(arr))    
    # ///////////////////////////////////////////////////////////////////////////////////
