import sys
from collections import deque

t = int(input())

for _ in range(t):
    w, h = map(int, sys.stdin.readline().split())
    graph = [list(sys.stdin.readline().strip()) for _ in range(h)]

    # 초기 상근이 위치 
    pos_x, pos_y = 0, 0
    # 초기 불이 붙어있는 지점 파악 
    fire = deque()

    # 시작 위치, 불 위치 찾기
    for i in range(h):
        for j in range(w):
            if graph[i][j] == "@":
                pos_x, pos_y = i, j
            elif graph[i][j] == "*":
                fire.append((i, j))

    # 탐색
    dxs = [0, 0, 1, -1]
    dys = [1, -1, 0, 0]
    visited = [[0]*w for _ in range(h)]
    pos_q = deque([(pos_x, pos_y)])
    visited[pos_x][pos_y] = 1

    # 상근이가 더 이동할 수 있는 곳이 없을 때 까지 
    while pos_q:
        # 현재 시점에서 불이 붙어있는 곳들에서 다음 시점에 불이 붙을 곳 탐색  
        fire_len = len(fire)
        for _ in range(fire_len):
            fx, fy = fire.popleft()
            for dx, dy in zip(dxs, dys):
                fnx, fny = dx + fx, dy + fy
                if -1 < fnx < h and -1 < fny < w and graph[fnx][fny] != "#" and graph[fnx][fny] != "*":
                    graph[fnx][fny] = "*"
                    # 다음 시점에서 불이 붙어 있는 곳 저장 
                    fire.append((fnx, fny))

        # 현재 시점에서 상근이가 이동가능한 후보들에서 다음 시점의 이동 가능지역 탐색
        pos_len = len(pos_q)
        for _ in range(pos_len):
            x, y = pos_q.popleft()
            for dx, dy in zip(dxs, dys):
                nx, ny = dx + x, dy + y
                if -1 < nx < h and -1 < ny < w and not visited[nx][ny] and graph[nx][ny] == ".":
                    # 방문 처리 및 이동 횟수 기록
                    visited[nx][ny] = visited[x][y] + 1
                    # 다음 시점에서 이동 가능한 곳 저장
                    pos_q.append((nx, ny))

    # 이동이 끝난 후 visited 배열을 보았을 때
    # 지도의 가에 위치한 곳에서 0이 아닌 수가 있다면 상근이가 탈출했다는 뜻
    ans = sys.maxsize
    for i in range(h):
        for j in range(w):
            # 첫 번째 행과 마지막 행
            if i == 0 or i == h-1:
                if visited[i][j] != 0:
                    ans = min(visited[i][j], ans)
            # 첫 번째 열과 마지막 열 
            if j == 0 or j == w-1:
                if visited[i][j] != 0:
                    ans = min(visited[i][j], ans)

    if ans == sys.maxsize:
        print("IMPOSSIBLE")
    else:
        print(ans)