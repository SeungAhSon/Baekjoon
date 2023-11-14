import sys

N = int(sys.stdin.readline())

word_dict = {'ChongChong':[]}

for _ in range(N):
  A,B = sys.stdin.readline().strip().split()
  if A in word_dict.keys():
    word_dict[A].append(B)
    word_dict[B] = []
  if B in word_dict.keys():
    word_dict[B].append(A)
    word_dict[A] = []
  
  
print(len(word_dict.items()))