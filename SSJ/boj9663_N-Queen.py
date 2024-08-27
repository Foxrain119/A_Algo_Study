# python3로 컴파일하면 시간초과...
# pypy3로 해야 정답

def dfs(r):
    global cnt

    if r == n:
        cnt += 1
        return

    for i in range(n):
        if check(r, i):    
            visited[r] = i
            dfs(r + 1)
            # visited[r] = 0 필요 없음 > 어차피 반복문 돌면 다른 값으로 바뀜.

def check(r, x):
    for j in range(r):
        if (x == visited[j]) or (x == (r + visited[j] - j)) or (x == (j + visited[j] - r)): # 열, 오른 대각선(쉣), 왼쪽 대각선 순서
            return False
    return True

n = int(input())
visited = [0] * n
cnt = 0

dfs(0)
print(cnt)