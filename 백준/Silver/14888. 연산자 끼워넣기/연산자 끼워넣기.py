N = int(input())
A = list(map(int, input().split()))
a,b,c,d  = map(int, input().split())

max_ans = -float('inf')
min_ans = float('inf')

def dfs(depth,ans, a,b,c,d):
  global max_ans, min_ans
  
  if depth == N : 
    max_ans = max(max_ans, ans)
    min_ans = min(min_ans, ans)
  
  if a:
    dfs(depth+1,ans+A[depth], a-1,b,c,d)
  if b:
    dfs(depth+1,ans-A[depth], a,b-1,c,d)
  if c:
    dfs(depth+1,ans*A[depth], a,b,c-1,d)
  if d:
    dfs(depth+1,int(ans/A[depth]),a,b,c,d-1)
      

dfs(1,A[0],a,b,c,d)
  
print(max_ans)
print(min_ans)

