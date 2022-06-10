import math

def isprimenumber(x):
    for i in range (2, int(math.sqrt(x) + 1)):
    	if x % i == 0: return False
    return True

prime = []
for i in range(2,246913):
    if isprimenumber(i) : prime.append(i)

while(1) :
    N = int(input())
    if N==0 : break
    count = 0
    
    for i in prime :
        if N<i<=2*N: count += 1
    print(count)