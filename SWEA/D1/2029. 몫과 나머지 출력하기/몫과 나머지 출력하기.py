T = int(input())
for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    print("#",test_case," ",a//b," ",a%b,sep = "")