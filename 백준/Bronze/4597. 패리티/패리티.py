while True:
    bitString = input()
    if bitString == '#': break

    ans = bitString[:-1]
    bitCnt = bitString.count('1')
    if bitString[-1] == 'e':
        if bitCnt % 2 == 0: print(ans+'0')
        else: print(ans+'1')
    else:
        if bitCnt % 2 == 0: print(ans+'1')
        else: print(ans+'0')