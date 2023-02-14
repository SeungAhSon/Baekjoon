N = int(input())
player = []
ans=[]
 
for _ in range(N):
       name = input()
       player.append(name[0])

names = sorted(set(player))
for i in names:
       if player.count(i) >= 5:
            ans.append(i)

if len(ans) > 0: print(''.join(ans))
else: print("PREDAJA")