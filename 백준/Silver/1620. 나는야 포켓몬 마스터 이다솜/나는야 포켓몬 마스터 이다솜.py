'''
#첫 시도
#시간 초과

import sys
N,M = map(int, sys.stdin.readline().split())

pokemon = ['0']
for _ in range(N):
    temp = sys.stdin.readline().lower()[:-1]
    if temp not in pokemon : pokemon.append(temp)

for i in range(M):
    temp = sys.stdin.readline()[:-1]
    if temp.isdigit(): print(pokemon[int(temp)][0].upper()+pokemon[int(temp)][1:])
    else : print(pokemon.index(temp.lower()))
'''


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