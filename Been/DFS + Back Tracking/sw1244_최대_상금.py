def per(l, r, depth, state):
    if l < r:
        return 0
    if depth == N:
        return 1
    if dp[state]:
        return dp[state]
    cnt = 0
    for i in range(N):
        if visit[i] == False:
            visit[i] = True
            cnt += per(l + weights[i], r, depth + 1, state + dpn[i])
            if l >= r + weights[i]:
                cnt += per(l, r + weights[i], depth + 1, state + dpn[i] * 2)
            visit[i] = False
    dp[state] = cnt
    return cnt


T = int(input())
for t in range(T):
    N = int(input())
    weights = list(map(int, input().split()))
    dpn = [1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049]
    dp = [0] * dpn[N]
    visit = [False] * N
    print('#{} {}'.format(t + 1, per(0, 0, 0, 0)))