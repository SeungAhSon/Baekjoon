T = int(input())
score_dict = ['A+','A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for tc in range(1, T+1):
    N, K = map(int, input().split())
    score = []
    for _ in range(N):
        a,b,c = map(int, input().split())
        score.append(a*0.35+b*0.45+c*0.20)
    k_score = score[K-1]

    score.sort(reverse= True)
    temp = score.index(k_score) // (N//10)
   
    print("#{} {}".format(tc, score_dict[temp]))