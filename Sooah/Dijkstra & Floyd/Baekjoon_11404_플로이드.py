n = int(input()) # 도시 수
m = int(input()) # 버스 수
bus = [[float('inf')]*(n+1) for _ in range(n+1)]

# 바로 연결된 간선 채우기
for _ in range(m):
    a, b, c = map(int, input().split()) # (시작도시, 도착도시, 비용)
    if c < bus[a][b]:
        bus[a][b] = c

# 자기자신으로 가는 거리는 0
for i in range(n+1):
    bus[i][i] = 0

# 한 번씩 거쳐가는 거리가 바로 가는 거리보다 작다면, 갱신
for mid in range(n+1):
    for i in range(n+1):
        if i == mid: continue
        for j in range(n+1):
            if i == j or j == mid:
                continue
            new = bus[i][mid] + bus[mid][j]
            if bus[i][j] > new:
                bus[i][j] = new
                
# 갈 수 없는 경로는 0으로 처리
for i in range(n+1):
    for j in range(n+1):
        if bus[i][j] == float('inf'):
            bus[i][j] = 0

for row in bus[1:]:
    print(*row[1:])