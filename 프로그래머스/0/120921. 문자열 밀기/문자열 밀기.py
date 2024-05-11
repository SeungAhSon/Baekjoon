#7번 반례 : "abc", "bca", "2"
def solution(A, B):
    for i in range(len(A)+1):
        if A==B: return i
        A = A[-1]+A[:-1]
    return -1