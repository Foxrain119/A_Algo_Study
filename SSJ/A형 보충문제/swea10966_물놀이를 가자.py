# import sys
from collections import deque
# sys.stdin = open('10966.txt', 'r')

def bfs():
    dq = deque(water)
    for r, c in water:
        visited[r][c] = 0
    
    while dq:
        for _ in range(len(dq)):
            pr, pc = dq.popleft()
            for k in range(4):
                npr = pr + drow[k]
                npc = pc + dcol[k]
                # 인덱스 조건을 만족하고, 방문하지 않았다면 덱에 넣어준다 -> 이미 방문 했다면 다른 water에서 해당 land까지 도착하는데 걸리는 시간이 더 짧기 때문!!!
                # if 0 <= npr < n and 0 <= npc < m and visited[npr][npc] == float('Inf'): -> test case 18번에서 런타임 에러(시간 초과)
                if 0 <= npr < n and 0 <= npc < m and visited[npr][npc] == -1:
                    visited[npr][npc] = visited[pr][pc] + 1
                    dq.append((npr, npc))

t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())
    grid = [input() for _ in range(n)]
    # 네 방향 탐색
    drow = [-1, 0, 1, 0]
    dcol = [0, 1, 0, -1]
    water = []
    # 이동 횟수를 저장하는 visited 리스트
    # visited = [[float('Inf')] * m for _ in range(n)] -> test case 18번에서 런타임 에러(시간 초과) -> 실행시간 6,000ms up
    visited = [[-1] * m for _ in range(n)] # 단지 -1로 바꿔줬을 뿐인데 실행시간 3,115ms -> float('Inf')는 사용하지 말자

    # 물 위치 좌표 저장
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'W':
                water.append((i, j))

    bfs()

    result = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'L':
                result += visited[i][j]

    print(f'#{tc} {result}')
