n = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

sorted_a = sorted(A, reverse=True)
sorted_b = sorted(B)

s = [sorted_a[i]*sorted_b[i] for i in range(n)]

print(sum(s))