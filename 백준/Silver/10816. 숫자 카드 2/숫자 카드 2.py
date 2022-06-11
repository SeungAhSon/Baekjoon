import sys

def binary_search(N, N_list, start, end):
    if(start>end): return 0
    mid = (start+end)//2
    if(N==N_list[mid]): return count.get(N)
    elif(N<N_list[mid]): return binary_search(N, N_list, start, mid-1)
    elif(N>N_list[mid]): return binary_search(N, N_list, mid+1, end)

N = int(sys.stdin.readline())
N_list = sorted([*map(int, sys.stdin.readline().split())])

M = int(sys.stdin.readline())
M_list = [*map(int, sys.stdin.readline().split())]

count = {}
for i in N_list:
    if i in count : count[i]+=1
    else : count[i]=1

for temp in M_list:
    print(binary_search(temp,N_list,0,N-1), end=" ")