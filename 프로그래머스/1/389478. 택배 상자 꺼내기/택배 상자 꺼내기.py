def solution(n, w, num):
    h = (n + w - 1) // w
    
    positions = dict()
    box = 1
    for i in range(h):
        if i % 2 == 0: 
            for j in range(w):
                if box > n:
                    break
                positions[box] = (i, j)
                box += 1
        else:  # 오른쪽 → 왼쪽
            for j in reversed(range(w)):
                if box > n:
                    break
                positions[box] = (i, j)
                box += 1
    
    target_floor, target_col = positions[num]
    
    count = 0
    for box_num, (floor, col) in positions.items():
        if col == target_col and floor >= target_floor:
            count += 1
    return count
