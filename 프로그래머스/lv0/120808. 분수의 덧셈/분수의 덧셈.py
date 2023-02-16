def solution(numer1, denom1, numer2, denom2):
    ans_denom = denom1*denom2
    ans_num = numer1*denom2 + numer2*denom1
    
    #약분
    divisor=1
    for i in range(min(ans_denom, ans_num),0,-1):
        if ans_denom%i == 0 and ans_num%i == 0:    
            divisor = i
            break
    return [ans_num//divisor, ans_denom//divisor]