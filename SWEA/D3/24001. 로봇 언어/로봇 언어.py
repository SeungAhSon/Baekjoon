def solve_answer(arr, flag):
    x = 0
    max_dist = 0
    
    for i in arr:
        if i=='L': x-=1
        elif i=='R': x+=1
        else:
            if flag: x-=1
            else: x+=1
        max_dist = max(max_dist, abs(x))
		
    return max_dist


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    arr = list(input())
    x1 = solve_answer(arr, 0)
    x2 = solve_answer(arr, 1)

    print(max(x1,x2))
    # //////////////////////////////////////////////////////////////////////////////////