def solution(numlist, n):
    new_numlist = [(i, abs(i-n)) for i in numlist]
    new_numlist.sort(key=lambda x:(x[1],-x[0]))

    return [i[0] for i in new_numlist]