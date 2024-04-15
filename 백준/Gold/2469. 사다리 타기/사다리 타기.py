import sys

#input 
K = int(sys.stdin.readline()) #참가한 사람의 수
N = int(sys.stdin.readline()) #행 수
fin_ppl = list(sys.stdin.readline().rstrip())
start_ppl = sorted(fin_ppl)

q_row = 0
ladder = []
for i in range(N):
  temp = sys.stdin.readline().rstrip()
  if temp[0] =='?': q_row=i
  ladder.append(temp)

#solve
up_ppl = start_ppl.copy() #위에서부터 내려오기
down_ppl = fin_ppl.copy() #아래에서부터 올라오기

for i in range(K):
  temp = i #현재 위치 저장
  for j in range(0, q_row):
    if temp<K-1 and ladder[j][temp]=="-":  temp+=1
    elif 0<temp and ladder[j][temp-1]=="-":  temp-=1
  up_ppl[temp]=start_ppl[i]
  
for i in range(K):
  temp = i #현재 위치 저장
  for j in range(N-1, q_row, -1):
    if temp<K-1 and ladder[j][temp]=="-":  temp+=1
    elif 0<temp and ladder[j][temp-1]=="-":  temp-=1
  down_ppl[temp]=fin_ppl[i]

q_ans = [""]*(K-1)
for i in range(K-1):
  if up_ppl[i]==down_ppl[i]: 
    q_ans[i]='*'
  elif (i<K-1) and (up_ppl[i]==down_ppl[i+1]) and (up_ppl[i+1]==down_ppl[i]):
    q_ans[i]='-'
    tmp=up_ppl[i]
    up_ppl[i]=up_ppl[i+1]
    up_ppl[i+1]=tmp
  else:
    q_ans = ["x"]*(K-1)
    break
    
print(''.join(q_ans))