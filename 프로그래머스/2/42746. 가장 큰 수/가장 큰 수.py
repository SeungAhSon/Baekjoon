def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x: 3*x, reverse = True)
    return str(int(''.join(numbers)))