from collections import defaultdict
def solution(polynomial):
    poly_dic = defaultdict(int)
    poly = list(map(str,polynomial.split(" + ")))
    for i in range(len(poly)):
        if (poly[i][-1] == "x"):
            poly_dic['x'] += int(poly[i].replace('x',''))
        else:
            poly_dic['-'] += int(poly[i])
    answer = poly_dic['x'] + 'x' + poly_dic['-']
    return answer