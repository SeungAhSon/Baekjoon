def solution(cipher, code):
    answer = [cipher[code*i-1] for i in range(1, len(cipher)//code+1)]
    return ''.join(answer)