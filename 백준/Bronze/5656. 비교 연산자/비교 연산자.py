import sys

i = 1
while True : 
  a,E,b = sys.stdin.readline().split()
  if E == "E" : break

  a,b = int(a), int(b)
  if E==">" : print(f"Case {i}: {str(a>b).lower()}")
  elif E==">=" : print(f"Case {i}: {str(a>=b).lower()}")
  elif E=="<" : print(f"Case {i}: {str(a<b).lower()}")
  elif E=="<=" : print(f"Case {i}: {str(a<=b).lower()}")
  elif E=="==" : print(f"Case {i}: {str(a==b).lower()}")
  elif E=="!=" : print(f"Case {i}: {str(a!=b).lower()}")
  i+=1

