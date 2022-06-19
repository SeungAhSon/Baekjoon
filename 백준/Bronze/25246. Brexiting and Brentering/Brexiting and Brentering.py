vowel = ['a','e','i','o','u','A',"E","I","O","U"]

word = input()

for i in range(len(word)-1,-1,-1):
    if word[i] in vowel : 
        print(word[0:i+1]+"ntry")
        break