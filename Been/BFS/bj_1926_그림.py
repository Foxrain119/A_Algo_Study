from collections import deque


# 섬 넓이 구하는 함수
def bfs():
    count = 1  # 시작 넓이
    while queue:
        i, j = queue.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni < 0 or nj < 0 or ni >= N or nj >= M:
                continue
            if graph[ni][nj] == 1 and visited[ni][nj] == 0:
                queue.append((ni, nj))
                visited[ni][nj] = 1
                count += 1
    return count


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

queue = deque([])
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
cnts = 0  # 섬 갯수
extent = 0  # 가장 넓은 섬 넓이

# 방문하지 않은 섬 카운팅, bfs 로 넓이 구하기
for i in range(N):
    for j in range(M):
        # 방문 안한 섬이면 bfs 함수 실행
        if graph[i][j] == 1 and visited[i][j] == 0:
            queue.append((i, j))
            visited[i][j] = 1
            cnts += 1
            ext = bfs()
            # 더 넓으면 저장
            if ext > extent:
                extent = ext

print(cnts)
print(extent)
