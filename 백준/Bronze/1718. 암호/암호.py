import sys

s = list(sys.stdin.readline()[:-1])
key = sys.stdin.readline()[:-1]
key = key*(len(s)//len(key))+key[:len(s)%len(key)]

for i in range(len(s)):
    if s[i].isalpha():
        s[i] =chr((ord(s[i])-ord(key[i])-1)%26+97)

print(''.join(s))