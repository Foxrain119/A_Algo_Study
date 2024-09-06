from collections import deque

def bfs(i, j):
    dq = deque([(i, j)])
    visited[i][j] = grid[i][j]
    while dq:
        for _ in range(len(dq)):
            r, c = dq.popleft()
            for k in range(4):
                nr = r + dxy[k][0]
                nc = c + dxy[k][1]

                if nr < 0 or nr >= n or nc < 0 or nc >= n:
                    continue
                
                # 현재 시점에서 다음 경로로 이동할 때 공사 시간이 더 길다면 -> 버려
                # 자연스럽게 가지치기가 된다.
                # BOJ_달리기와 비슷한 문제같다.
                if visited[r][c] + grid[nr][nc] >= visited[nr][nc]:
                    continue

                visited[nr][nc] = visited[r][c] + grid[nr][nc]
                dq.append((nr, nc))


t = int(input())

for tc in range(1, t + 1):
    n = int(input()) # 정사각형 지도 변의 길이
    grid = [list(map(int, list(input()))) for _ in range(n)]

    visited = [[float('Inf')] * n for _ in range(n)]
    dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 우, 하, 좌, 상

    bfs(0, 0)

    print(f'#{tc} {visited[n - 1][n - 1]}')