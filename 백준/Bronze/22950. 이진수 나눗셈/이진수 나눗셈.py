N = int(input())
M = input()
K = int(input())
if(int('0b'+M,2)%2**K==0) : print("YES")
else : print("NO")