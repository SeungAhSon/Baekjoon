import sys
sys.setrecursionlimit(10000)

def recursion(temp, div_3):
  if div_3<3: return '-'
  div_3 = div_3//3
  temp2 = recursion(temp, div_3)
  return temp2+' '*div_3+temp2
  
while(True):
  read_num = sys.stdin.readline()
  if read_num=='': break
  N = int(read_num)
  
  temp = '-'*(3**N)
  print(recursion(temp, 3**N))