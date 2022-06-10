import math

def isprimenumber(x):
    for i in range (2, int(math.sqrt(x) + 1)):
    	if x % i == 0: return False
    return True
    
    
prime = []
for i in range(2,10000) : 
    if isprimenumber(i) : prime.append(i)
    
    
T = int(input())
min = 10000

for i in range(T):
    temp = int(input())
    for j in range(temp//2,1,-1):
        if((j in prime) and ((temp-j) in prime)) :
            print(j, temp-j)
            break