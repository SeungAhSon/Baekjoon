import sys
#input은 EOF를 받을 때 EOFError를 일으키지만 
#sys.stdin.readline은 EOF를 받을 때 빈 문자열을 리턴

TXTMSG_map = {
  "CU": "see you",
  ":-)": "I’m happy",
  ":-()": "I’m unhappy",
  ";-)": "wink",
  ":-P": "stick out my tongue",
  "(~.~)": "sleepy",
  "TA": "totally awesome",
  "CCC": "Canadian Computing Competition",
  "CUZ": "because",
  "TY": "thank-you",
  "YW": "you’re welcome",
  "TTYL": "talk to you later"
}
  
while True:
  temp = sys.stdin.readline().rstrip()
  if temp=="": break
  if temp in TXTMSG_map: print(TXTMSG_map[temp])
  else: print(temp)