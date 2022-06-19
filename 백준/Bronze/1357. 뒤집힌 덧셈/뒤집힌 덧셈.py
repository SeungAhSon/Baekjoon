A,B = map(str,input().split())

A = list(reversed(A))
B = list(reversed(B))

ans = int("".join(A)) + int("".join(B))
print(int("".join(list(reversed(str(ans))))))