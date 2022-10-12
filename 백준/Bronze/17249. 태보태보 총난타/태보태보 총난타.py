left = 0
right = 0
TaeBo = input()

flag = 0

for i in TaeBo:
	if i=="(": flag = 1
	
	if flag == 0 and i=="@": left += 1
	elif flag == 1 and i=="@" : right += 1

print(left, right, sep = " ")