from collections import deque


# 직진 함수
# 시간 값과 방향 값, 이동 가능한 횟수 값을 넣어 직진
def go_straight(time, x, y, direction, cnt):
    ni = x + di[direction]
    nj = y + dj[direction]
    # 이동 가능할 때 까지 이동
    while cnt > 0:
        # 운동장 범위 안, 벽이 아닐 때 좌우 탐색 + 시간 값으로 체킹(운동장에)
        if 0 <= ni < N and 0 <= nj < M:
            if place[ni][nj] == '#':
                return
            elif place[ni][nj] == '.':
                if ni == x2 and nj == y2:
                    print(time)
                    exit()
                place[ni][nj] = time
                bfs(time, ni, nj, direction)
                if cnt == 1:
                    heap.append((time + 1, ni, nj, direction))
            # 시간이 동일한데 다른 방향에서 체킹 되어있을 경우, 그대로 직진
            elif place[ni][nj] == time:
                cnt -= 1
                ni += di[direction]
                nj += dj[direction]
                continue
            else:
                return
        else:
            return
        cnt -= 1
        ni += di[direction]
        nj += dj[direction]


# 좌우 길 탐색
def bfs(time, x, y, direction):
    for k in range(4):
        # 가는 방향, 뒤 탐색 x
        if k == direction and (k+2) % 4 == direction:
            continue
        ni = x + di[k]
        nj = y + dj[k]
        if 0 <= ni < N and 0 <= nj < M:
            if place[ni][nj] == '#':
                continue
            elif place[ni][nj] == '.':
                heap.append((time + 1, x, y, k))
            # 시간이 같거나 작을 경우 진행
            elif place[ni][nj] >= time + 1:
                heap.append((time + 1, x, y, k))


# Start
N, M, K = map(int, input().split())
place = [[] for _ in range(N)]  # 운동장
for i in range(N):
    place[i] = list(input().strip())
# 시간 순서대로 append 하고 popleft 하기위해 덱 사용
heap = deque()

# 초기 값 설정
x1, y1, x2, y2 = map(int, input().split())
x1 -= 1; y1 -= 1; x2 -= 1; y2 -= 1
if x1 == x2 and y1 == y2:
    print(0)
    exit()
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
place[x1][y1] = 0
for k in range(4):
    ni = x1 + di[k]
    nj = y1 + dj[k]
    if 0 <= ni < N and 0 <= nj < M and place[ni][nj] == '.':
        heap.append((1, x1, y1, k))

while heap:
    a, b, c, d = heap.popleft()
    go_straight(a, b, c, d, K)
else:
    print(-1)
