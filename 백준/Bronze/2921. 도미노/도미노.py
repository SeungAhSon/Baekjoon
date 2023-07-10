N = int(input())
domino = [1.5*i*(i+1) for i in range(1,N+1)]
print(int(sum(domino)))