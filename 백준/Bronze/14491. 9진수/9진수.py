N = int(input())

rev_base = ''

while N > 0:
    N, mod = divmod(N, 9)
    rev_base += str(mod)
print(rev_base[::-1])