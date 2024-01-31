a, b = map(int, input().split())

if a==1:
  if b==2: print("B")#가위, 바위
  elif b==3: print("A")#가위, 보

elif a==2 :
  if b==1:print("A")  #바위, 가위
  elif b==3:print("B")  #바위, 보
  
else:
  if b==1:print("B")  #보, 가위
  elif b==2:print("A")  #보, 바위
  
  
