import sys
N = int(sys.stdin.readline())
birthday = []

for _ in range(N):
    Name,Day,Month,Year = sys.stdin.readline().split()
    Day,Month,Year = map(int,(Day,Month,Year))
    birthday.append((Year,Month,Day,Name))
birthday.sort()
print(birthday[N-1][3])
print(birthday[0][3])