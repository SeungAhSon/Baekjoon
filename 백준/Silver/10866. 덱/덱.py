#그냥 input으로 받으면 시간초과
import sys

N = int(sys.stdin.readline())

Deque = []
def pop_front():
    if(len(Deque)==0) : return -1
    else : return Deque.pop(0)
    
def pop_back():
    if(len(Deque)==0) : return -1
    else : return Deque.pop()

def empty():
    if(len(Deque)==0) : return 1
    else : return 0

def front():
    if(len(Deque)==0) : return -1
    else : return Deque[0]
    
def back():
    if(len(Deque)==0) : return -1
    else : return Deque[-1]


for _ in range(N):
    order = sys.stdin.readline().split()
    if order[0][:4]=="push": 
        if order[0][5]=="f" : Deque.insert(0,order[1])
        else : Deque.append(order[1])
            
    elif order[0][:3]=="pop" : 
        if order[0][4] == "f": print(pop_front())
        else : print(pop_back())
    
    elif order[0] =="size": print(len(Deque))
    elif order[0] =="empty": print(empty())
    elif order[0] == "front": print(front())
    elif order[0] =="back": print(back())