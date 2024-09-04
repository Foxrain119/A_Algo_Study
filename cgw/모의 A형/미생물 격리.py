import heapq

t = int(input())

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

for tc in range(1, t+1):
    n, m, k = map(int, input().split())
    ans = 0
    info = dict()
    heap = []
    for i in range(k):
        info[i] = list(map(int, input().split()))

    while m > 0:
        visited = [[-1] * n for _ in range(n)]
        # 이동
        for i, val in info.items():
            if val != -1:
                x, y, num, direction = val
                nx, ny = dxs[direction-1]+x, dys[direction-1]+y
                # 경계
                if nx == 0 or nx == n-1 or ny == 0 or ny == n-1:
                    if num//2 == 0:
                        info[i] = -1
                        continue
                    info[i][2] = num // 2
                    if direction%2 != 0: info[i][3] += 1
                    else: info[i][3] -= 1
                info[i][0], info[i][1] = nx, ny
                heapq.heappush(heap, (-info[i][2], info[i][0], info[i][1], info[i][3], i))

        while heap:
            num, x, y, direction, i = heapq.heappop(heap)  # num은 음수
            if visited[x][y] == -1:
                visited[x][y] = i
            else:
                if info[visited[x][y]] != -1:
                    info[visited[x][y]][2] += -num
                    info[i] = -1
        m -= 1

    for idx, val in info.items():
        if val != -1:
            ans += val[2]
    print(f"#{tc} {ans}")