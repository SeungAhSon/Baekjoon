def solution(slice, n):
    return n//slice + (1 if n%slice!=0 else 0)