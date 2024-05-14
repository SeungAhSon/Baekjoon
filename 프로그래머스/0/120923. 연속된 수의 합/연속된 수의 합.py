def solution(num, total):
    # 등차수열의 합 : n*(start+end)/2
    # ==> total = num*(s+s+num-1)/2
    # ==> s = (total/num*2-num+1)/2
    s = int((total/num*2-num+1)/2)
    return [i for i in range(s, s+num, 1)]