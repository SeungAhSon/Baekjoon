T = int(input())

for _ in range(T):
    name = list(input().split())
    start_index = name.index(input())
    gum = int(input())
    print(name[(start_index+gum-1)%len(name)])