import sys
N,M = map(int, sys.stdin.readline().split())

pokemon_num2name = {}
pokemon_name2num = {}

for i in range(1,N+1):
    temp = sys.stdin.readline()[:-1]
    pokemon_name2num[temp]=i
    pokemon_num2name[i]=temp

for i in range(M):
    temp = sys.stdin.readline()[:-1]
    if temp.isdigit(): print(pokemon_num2name[int(temp)])
    else : print(pokemon_name2num[temp])