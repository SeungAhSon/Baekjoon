N = input()
N_list = list(N)
N_len = len(N_list)

k = -1
for i in range(N_len - 1):
    if N_list[i] < N_list[i + 1]: k = i

l = -1
for i in range(k + 1, N_len):
    if N_list[k] < N_list[i]:    l = i
N_list[k], N_list[l] = N_list[l], N_list[k]
N_list = N_list[:k + 1] + N_list[k + 1:][::-1]

print(''.join(N_list))
