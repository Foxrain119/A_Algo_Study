import sys
from collections import deque

n, m, k = map(int, sys.stdin.readline().split())
graph = [sys.stdin.readline().strip() for _ in range(n)]
start_x, start_y, dest_x, dest_y = map(int, sys.stdin.readline().split())
start_x, start_y, dest_x, dest_y = start_x-1, start_y-1, dest_x-1, dest_y-1

dxs = [0, 0, 1, -1]
dys = [1, -1, 0, 0]
MAXSIZE = 99999999

visited = [[MAXSIZE]*m for _ in range(n)]

q = deque([[start_x, start_y, 0]])
visited[start_x][start_y] = 0

while q:

    x, y, cnt = q.popleft()

    for dx, dy in zip(dxs, dys):
        for i in range(1, k+1):
            nx, ny = dx*i+x, dy*i+y
            if -1 < nx < n and -1 < ny < m and graph[nx][ny] != "#" and visited[nx][ny] > cnt:
                if visited[nx][ny] == MAXSIZE:
                    visited[nx][ny] = cnt + 1
                    q.append([nx, ny, cnt + 1])
            
            else:
                break

if visited[dest_x][dest_y] == MAXSIZE:
    print(-1)
else:
    print(visited[dest_x][dest_y])