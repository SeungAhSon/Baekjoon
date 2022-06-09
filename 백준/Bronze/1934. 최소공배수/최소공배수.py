#이중 for문을 사용하니 시간초과가 났다.
#최대공약수를 유클리드 호제법을 활용해 계산한 뒤,
#최소공배수는 x,y를 곱한 값을 최대공약수로 곱해주면 얻을 수 있다.

T = int(input())

def gcd(x, y):
   while y: x, y = y, x % y
   return x
   
for i in range(T):
    A,B = map(int,input().split())
    print(A*B//gcd(A,B))
