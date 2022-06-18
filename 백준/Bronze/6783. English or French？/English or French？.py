#4447번 좋은놈 나쁜놈 문제와 같은 구성이다.
import sys

N = int(sys.stdin.readline())

countT = 0
countS = 0
for _ in range(N):
    text = sys.stdin.readline().rstrip('\n')
    countT += text.count('t') + text.count("T")
    countS += text.count('s') + text.count("S")
    
if countT>countS : print("English")
else : print("French")