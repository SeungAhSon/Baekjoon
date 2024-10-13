def solution(tickets):
    for i in tickets: i.append(0)
    tickets.sort(key=lambda x:x[1])
    t = ["ICN"]
    
    def dfs(port):
        for i in tickets:
            if i[0]==port and i[2]==0:
                t.append(i[1])
                i[2]=1
                
                if len(t)==len(tickets)+1 or dfs(i[1]): return t

                i[2]=0
                t.pop()
    
    answer = dfs("ICN")
    return answer
