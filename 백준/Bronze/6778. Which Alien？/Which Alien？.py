import sys

A = int(sys.stdin.readline())
E = int(sys.stdin.readline())

if A >= 3 and E <= 4:    print("TroyMartian")
if A <= 6 and E >= 2:    print("VladSaturnian")
if A <= 2 and E <= 3:    print("GraemeMercurian")