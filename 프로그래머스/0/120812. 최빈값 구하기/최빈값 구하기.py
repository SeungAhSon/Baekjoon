def solution(array):
    array.sort()
    countdict = {x:array.count(x) for x in array}
    ans = [k for k,v in countdict.items() if max(countdict.values()) == v]
    return -1 if len(ans)>1 else ans[0]