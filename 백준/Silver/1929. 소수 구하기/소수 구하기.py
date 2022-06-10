import math

#1*25 = 25
#5*5 = 25
#25*1 = 25
#약수는 제곱근을 기준으로 대칭을 이루기 때문에,
#소수인지 판별하려면 제곱근 까지만 확인하면 된다.

def isprimenumber(x):
    for i in range (2, int(math.sqrt(x) + 1)):
    	if x % i == 0: return False
    return True
    
M,N = map(int,input().split())
    
#만약 89%에서 틀렸다고 뜬다면,
#M = 1일 때 1부터 출력되는 문제가 있었기 때문이다.
if M==1 : M = 2
for i in range(M,N+1):
    if isprimenumber(i) : print(i)