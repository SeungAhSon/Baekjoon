import sys
input = sys.stdin.readline

def merge_sort(arr):
    if len(arr) == 1: return arr
    
    mid = (len(arr)+1)//2
   
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    i,j = 0,0
    temp = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            temp.append(left[i])
            ans.append(left[i])
            i+=1
        else:
            temp.append(right[j])
            ans.append(right[j])
            j+=1
    while i < len(left):
        temp.append(left[i])
        ans.append(left[i])
        i+=1
    while j < len(right):
        temp.append(right[j])
        ans.append(right[j])
        j+=1
    
    return temp

N, K = map(int,input().split())
a = list(map(int,input().split()))
ans = []
merge_sort(a)

print(ans[K-1] if len(ans) >= K else -1)