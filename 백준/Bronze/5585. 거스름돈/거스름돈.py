money = 1000-int(input())
count = 0

while(money>=500):
    money -= 500
    count += 1

while(money>=100):
    money -= 100
    count += 1

while(money>=50):
    money -= 50
    count += 1
    
while(money>=10):
    money -= 10
    count += 1

while(money>=5):
    money -= 5
    count += 1
    
print(count+money)