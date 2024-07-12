#테스트케이스 25개 중 23개 통과. 다음에 고려하지 못한 사항 찾아내야 한다.
#답안지는 dfs를 사용한다.

def into_original_series(element, original_series, original_partial_sum):
    original_series.append(element)
    new_sums = []
    for psum in original_partial_sum:
        new_sums.append(psum + element)
    original_partial_sum.extend(new_sums)
    original_partial_sum.append(element)
    original_partial_sum.sort()

def execute(N, partial_sum):
    original_series = []
    original_partial_sum = []

    for i in range(1, len(partial_sum)):
        if len(original_series) < N:
            if partial_sum[i] in original_partial_sum:
                if original_series and original_series[-1] == partial_sum[i]:
                    into_original_series(partial_sum[i], original_series, original_partial_sum)
                continue
            else:
                into_original_series(partial_sum[i], original_series, original_partial_sum)
                
    original_series.sort()
    return original_series

#===input===
N = int(input())
partial_sum = list(map(int, input().split()))
partial_sum.sort()
original_series = execute(N, partial_sum)
print(" ".join(map(str, original_series)))
