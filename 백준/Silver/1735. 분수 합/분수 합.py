def gcd(x, y):
   while y: x, y = y, x % y
   return x
   
A,B = map(int, input().split())
C,D = map(int, input().split())

print((A*D+B*C)//gcd(A*D+B*C,B*D), B*D//gcd(A*D+B*C,B*D))