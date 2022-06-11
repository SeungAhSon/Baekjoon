L = int(input())
string = input()
 
answer = 0
for i in range(len(string)):
    answer+=(ord(string[i])-96)*(31**i)
 
print(answer%1234567891)