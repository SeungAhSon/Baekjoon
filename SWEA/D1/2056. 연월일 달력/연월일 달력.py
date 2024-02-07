days= {'01':31,'02':28,'03':31,'04':30,'05':31,'06':30,'07':31,'08':31,'09':30,'10':31,'11':30,'12':31} #딕셔너리를 사용

T = int(input())
for tc in range(1, T+1):
  temp = input()
  year, month, day = temp[:4], temp[4:6], temp[6:]
  
  if 0<int(month)<13 and 0<int(day)<=days[month]: print("#{} {}/{}/{}".format(tc, year, month, day))
  else: print("#{} -1".format(tc))