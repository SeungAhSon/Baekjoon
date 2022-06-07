A,B,C = map(int, input().split())
D = int(input())

C = C+D

while C>=60:
    C = C-60
    B = B+1

while B>=60:
    B = B-60
    A = A+1
    
while A>=24 :
    A = A-24

print(A,B,C)