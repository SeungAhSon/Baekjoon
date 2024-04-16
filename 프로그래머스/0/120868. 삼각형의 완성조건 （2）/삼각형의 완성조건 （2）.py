def solution(sides):
    return len(set([i for i in range(1, min(1,sum(sides)))]+[i for i in range(max(sides)-min(sides)+1, max(sides)+min(sides))]))