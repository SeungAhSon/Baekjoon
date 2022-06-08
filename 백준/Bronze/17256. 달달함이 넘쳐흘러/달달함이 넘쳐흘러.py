ax, ay, az = map(int, input().split())
cx, cy, cz = map(int, input().split())

print(cx-az,cy//ay,cz-ax)

#cx = az+bx, cy = ay*by, cz = ax+bz 이므로
#bx = cx-az, by = cy/ay, bz = cz-ax