from itertools import permutations
temp = map(int, input().split(":"))
perm = list(permutations(temp))

count=0
for a,b,c in perm:
    if 1<=a<=12 and 0<=b<=59 and 0<=c<=59: count += 1

print(count)