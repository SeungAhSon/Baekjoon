def binary_search(n, ans_min, ans_max, times):
    #print(ans_min, ans_max)
    if ans_max < ans_min:  return -1

    mid = (ans_max + ans_min) // 2  # 중간값
    
    count = sum(mid//i for i in times)
    
    if count >= n  : ans_max = mid
    elif count < n : ans_min = mid
    if ans_min == ans_max-1 : return ans_max

    return binary_search(n, ans_min, ans_max, times) 

def solution(n, times):
    ans_min = min(times)
    ans_max = min(times)*n
    return binary_search(n, ans_min, ans_max, times)