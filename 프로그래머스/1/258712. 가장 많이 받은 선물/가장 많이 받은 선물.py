from collections import defaultdict

FM = {}
graph = []
giftScore = []

def splitFunc(s):
    ans = s.split(' ')
    graph[FM[ans[0]]][FM[ans[1]]] += 1
    graph[FM[ans[1]]][FM[ans[0]]] -= 1
    giftScore[FM[ans[0]]] += 1
    giftScore[FM[ans[1]]] -= 1

def solution(friends, gifts):
    global FM, graph, giftScore
    answer = 0
    giftScore = [0] * len(friends)
    
    for i, friend in enumerate(friends):
        FM[friend] = i
    
    graph = [[0] * len(friends) for _ in range(len(friends))]
    
    for gift in gifts:
        splitFunc(gift)
    
    for i in range(len(friends)):
        nowGift = 0
        for j in range(len(friends)):
            if graph[i][j] > 0:
                nowGift += 1
            elif graph[i][j] == 0:
                if giftScore[i] > giftScore[j]:
                    nowGift += 1
        if nowGift > answer:
            answer = nowGift
    
    return answer
