import sys

N = int(sys.stdin.readline())
words_list = []
ans_list = []
mark = -1
for i in range(N):
    word = sys.stdin.readline().rstrip()
    words_list.append(word)
    if word == "?":
        mark = i

T = int(sys.stdin.readline())

for _ in range(T):
    ans_list.append(sys.stdin.readline().rstrip())
if N == 1:
    print(ans_list[0])
else:
    for answer_check in ans_list:
        if mark == 0:
            if answer_check[-1] == words_list[mark+1][0]:
                if answer_check not in words_list:
                    print(answer_check)
                    break
        elif mark == N - 1:
            if answer_check[0] == words_list[mark - 1][-1]:
                if answer_check not in words_list:
                    print(answer_check)
                    break
        else:
            if answer_check[0] == words_list[mark-1][-1]:
                if answer_check[-1] == words_list[mark+1][0]:
                    if answer_check not in words_list:
                        print(answer_check)
                        break