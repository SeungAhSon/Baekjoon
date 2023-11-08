import sys

#삼각형이 되는 조건: 가장 긴 변이 나머지 두 변의 합보다 작은 경우
a, b, c = map(int, sys.stdin.readline().split())
while True:
  temp = max([a,b,c])
  if 2*temp<sum([a,b,c]): #temp<=sum([a,b,c])-temp
    print(sum([a,b,c]))
    break
  
  if max(a,max(b,c))==a: a-=1
  elif max(a,max(b,c))==b: b-=1
  elif max(a,max(b,c))==c: c-=1

