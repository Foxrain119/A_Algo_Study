from collections import deque
dr = [-1, 1, 0, 0] # 방향배열
dc = [0, 0, -1, 1]
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    paths = [[-1] * M for _ in range(N)]    # W-L 거리 update
    dq = deque([])                          
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'W':
                dq.append((i, j))           # W 좌표 저장
                paths[i][j] = 0             # W 위치 표시

    while dq:
        r, c = dq.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if nr<0 or nc<0 or nr>=N or nc>=M or not paths[nr][nc]: # 범위를 벗어나거나 W 위치면 지나감
                continue
            if paths[nr][nc] == -1:             # L이면서 이전에 지나가지 않은 곳이면
                paths[nr][nc] = paths[r][c] + 1 # 거리+1 저장
                dq.append((nr, nc))

    cnt = 0
    for row in paths:
        cnt += sum(row)

    print(f'#{tc} {cnt}')
