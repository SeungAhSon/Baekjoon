while True:
    A,B = map(float,input().split())
    if (A==0 and B==0): break
    print('{:.3f}'.format((1-(B/A)**2)**0.5))
