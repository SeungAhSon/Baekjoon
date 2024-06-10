#1011과 유사한 문제 - 1011는 x<y, 4395는 x<=y
T = int(input()) 

for _ in range(T):
    x, y = map(int, input().split())
    d = y - x
    n = 0
    if x==y : print(0)
    else:
      while True:
          if d <= n*(n+1): break
          n += 1
      
      print(n*2-1 if d<=n**2 else n*2)