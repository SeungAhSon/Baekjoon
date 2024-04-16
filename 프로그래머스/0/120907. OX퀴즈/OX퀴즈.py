def solution(quiz):
    answer = []
    
    for i in quiz:
        a, b = i.split("=")
        answer.append("O" if eval(a)==int(b) else "X")

    return answer