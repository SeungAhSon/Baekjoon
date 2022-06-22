V=float(input())
vote = input()

count = float(sum((1 if i=="A" else 0) for i in vote))
if count>V/2 : print('A')
elif count==V/2 : print('Tie')
else: print('B')