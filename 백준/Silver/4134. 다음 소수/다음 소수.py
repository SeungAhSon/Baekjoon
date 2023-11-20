import sys
import math

def isprimenumber(x):
  if x==0 or x==1: return False
  
  for i in range (2, int(math.sqrt(x) + 1)):
    if x % i == 0: return False
  return True
    
T = int(sys.stdin.readline())
for _ in range(T):
  N = int(sys.stdin.readline())
  
  count = N
  while True:
    if isprimenumber(count) :
      print(count)
      break
    count+=1