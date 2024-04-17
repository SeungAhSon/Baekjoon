answer = [0,0]

def quad(arr, divider):
    global answer
    count = 0
    for row in arr:
        for value in row:
            if value == 1:  count += 1

    if count==divider*divider:   answer[1] += 1
    elif count==0:   answer[0] += 1
    else:
        if divider != 1:
            divider = divider // 2
            quad([i[:divider] for i in arr[:divider]], divider)
            quad([i[divider:] for i in arr[:divider]], divider)  
            quad([i[:divider] for i in arr[divider:]], divider) 
            quad([i[divider:] for i in arr[divider:]], divider)  

def solution(arr):
    global answer
    quad(arr, len(arr))
    return answer
