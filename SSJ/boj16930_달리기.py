import sys
input = sys.stdin.readline
from collections import deque

def bfs(r, c):
    dq = deque([(r, c)])
    visited[r][c] = 0
    while dq:
        for _ in range(len(dq)):
            x, y = dq.popleft()
            if x == (er - 1) and y == (ec - 1):
                return visited[x][y]
            for i in range(4):
                for j in range(1, k + 1):
                    nr = x + drow[i] * j
                    nc = y + dcol[i] * j
                    if nr < 0 or nr >= n or nc < 0 or nc >= m or grid[nr][nc] == '#' or visited[nr][nc] <= visited[x][y]: # 해당 지점을 이미 방문한 다른 경로가 더 효율적이라면 지금 택한 경로는 종료한다!!!
                        break
                    if visited[nr][nc] == sys.maxsize: # 더 최적화 > 선택 후보군 중 한 번도 방문해 보지 않은 경우라면 지금 경로를 계속 탐색한다 > 방문 해봤다면? 아니 이미 방문한 경로가 있는데 뭐하러 또 탐색해. 종료해
                        visited[nr][nc] = visited[x][y] + 1
                        dq.append((nr, nc))
    return -1

n, m, k = map(int, input().split())
grid = [input().rstrip() for _ in range(n)]
sr, sc, er, ec = map(int, input().split()) # start row, column / end row, column
drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]
visited = [[sys.maxsize] * m for _ in range(n)] # 해당 지점까지 이동하는데 걸린 시간을 담아주는 리스트

result = bfs(sr - 1, sc - 1) # 도착하기까지 걸린 시간을 출력
print(result)