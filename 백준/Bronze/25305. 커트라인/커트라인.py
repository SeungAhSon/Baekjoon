N, K = map(int, input().split())
student = list(map(int, input().split()))
print(sorted(student, reverse = True)[K-1])