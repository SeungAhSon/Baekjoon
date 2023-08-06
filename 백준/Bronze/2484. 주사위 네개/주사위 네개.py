import sys

N = int(sys.stdin.readline())

prizes = []
for _ in range(N):
    dice = [0]*7
    numbers = list(map(int, sys.stdin.readline().split()))
    
    for i in numbers: dice[i]+=1
    
    if(max(dice)==4) : prizes.append(50000+dice.index(4)*5000)
    elif(max(dice)==3) : prizes.append(10000+dice.index(3)*1000)
    elif(max(dice)==2) :
        temp = [i for i, value in enumerate(dice) if value == 2]
        if len(temp) == 2:
            prizes.append(2000+sum(temp)*500)
        else : prizes.append(1000+100*temp[0])
    elif(max(dice)==1) : prizes.append(max(numbers)*100)
    
print(max(prizes))