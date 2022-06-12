#단순한 합문제처럼 보이지만, 상대성 이론 광속 불변의 법칙을 적용해야한다.

A,B = map(float,input().split())
c = 299792458

print((A+B)/(1+(A*B)/(c*c)))
