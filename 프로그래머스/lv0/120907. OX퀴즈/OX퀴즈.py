def solution(quiz):
    answer = []
    
    for i in quiz:
        formula, z = i.split("=")
        formula = formula.split()
        
        if formula[1] == "+":
            formula = int(int(formula[0]) + int(formula[2]))
            
        elif formula[1] == "-":
            formula = int(int(formula[0]) - int(formula[2]))
        
        if formula == int(z) : answer.append("O")
        else : answer.append("X")

    return answer