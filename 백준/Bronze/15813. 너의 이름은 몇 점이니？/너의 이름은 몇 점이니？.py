N = int(input())
name = input()

ans = 0
for i in name:
    ans += ord(i)-64
    
print(ans)