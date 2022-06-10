T = int(input())

def gcd(x, y):
   while y: x, y = y, x % y
   return x
   
for _ in range(T):
    A,B = map(int,input().split())
    print(A*B//gcd(A,B), gcd(A,B))