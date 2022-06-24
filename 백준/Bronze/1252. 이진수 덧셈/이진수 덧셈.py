A,B = map(str, input().split())
print(bin(int('0b'+A,2)+int('0b'+B,2))[2:])