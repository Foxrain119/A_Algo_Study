def check(cnt):
    for i in range(cnt):
        if chess[cnt] == chess[i] or abs(chess[cnt] - chess[i]) == abs(cnt - i):
            return False
    return True


def n_queen(cnt):
    global ans
    if cnt == N:
        ans += 1
        return
    for i in range(N):
        chess[cnt] = i
        if check(cnt):
            n_queen(cnt + 1)


N = int(input())
chess = [0]*N
ans = 0
n_queen(0)
print(ans)
