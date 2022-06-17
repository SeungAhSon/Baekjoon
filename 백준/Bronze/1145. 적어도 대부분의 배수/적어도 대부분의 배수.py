from math import gcd
import itertools

def lcm(arr):
    ans = arr[0] 
    for num in arr:
        ans = ans*num // gcd(ans, num)     
    return ans
    
A = list(map(int, input().split()))

result = list(itertools.permutations(A,3))

temp = 1000000000
for i in result:
    temp = min(temp,int(lcm(i)))
    
print(int(temp))