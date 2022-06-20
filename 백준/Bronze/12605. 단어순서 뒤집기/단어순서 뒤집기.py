N = int(input())

for i in range(N):
    string = list(input().split())
    string.reverse()
    string =  " ".join(string)
    print("Case #%d: %s" %(i+1,string))