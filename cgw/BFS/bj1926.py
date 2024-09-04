from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

# 가장 큰 넓이를 갖는 그림의 넓이를 저장할 변수
ans = 0
# 그림의 개수 
pic_num = 0

dxs = [0, 0, 1, -1]
dys = [1, -1, 0, 0]

# 그림 찾기
for i in range(n):
    for j in range(m):
        # 1이고 이전에 방문한 적 없는 그림이라면 그림의 넓이를 구함 
        if graph[i][j] == 1 and not visited[i][j]:
            # 그림 개수 증가
            pic_num += 1

            # 넓이 구하기 
            # 넓이 == 시작점으로부터 도달할 수 있는 모든 칸의 개수 + 1(시작점)
            cnt = 1
            q = deque([(i, j)])
            visited[i][j] = True
            while q:
                x, y = q.popleft()
                for dx, dy in zip(dxs, dys):
                    nx, ny = dx+x, dy+y
                    if -1 < nx < n and -1 < ny < m and not visited[nx][ny] and graph[nx][ny] == 1:
                        # 넓이 증가 
                        cnt += 1
                        q.append((nx, ny))
                        visited[nx][ny] = True
            # 최대 넓이 갱신 
            ans = max(ans, cnt)
print(pic_num)
print(ans)