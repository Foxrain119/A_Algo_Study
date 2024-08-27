def dfs(i, j):
    cnt = 0
    stack = [(i, j)]
    while stack:
        x, y = stack.pop()
        if not visited[x][y]:
            visited[x][y] = 1
            cnt += 1
            for k in range(4):
                ni = x + drow[k]
                nj = y + dcol[k]
                if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and paper[ni][nj]:
                    stack.append((ni, nj))
    return cnt

n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
drow = [0, 1, 0, -1]
dcol = [1, 0, -1, 0]
visited = [[0] * m for _ in range(n)]
size = []

for x in range(n):
    for y in range(m):
        if paper[x][y] and not visited[x][y]:
            size.append(dfs(x, y))

print(len(size))
if len(size) > 0:
    print(max(size))
else:
    print(0)
