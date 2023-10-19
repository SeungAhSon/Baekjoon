import sys
from datetime import datetime

HH, MM = map(int, sys.stdin.readline().split())
ans = datetime(year=2022, month=1, day=1, hour=HH, minute=MM) - datetime(year=2022, month=1, day=1, hour=9)

print(ans.seconds // 60)