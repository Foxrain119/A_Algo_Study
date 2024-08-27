from collections import deque

def fire():
    for _ in range(len(fire_point)):
        x, y = fire_point.popleft()
        for k in range(4):
            ni = x + drow[k]
            nj = y + dcol[k]
            if ni < 0 or ni >= h or nj < 0 or nj >= w or building[ni][nj] == '#' or building[ni][nj] == '*':
                continue
            fire_point.append((ni, nj))

def escape():
    global flag2

    flag = 0 # if sanggeun can't move..ㅜㅜ
    for _ in range(len(sanggeun_point)):
        x, y = sanggeun_point.popleft()
        for k in range(4):
            ni = x + drow[k]
            nj = y + dcol[k]
            
            if ni < 0 or ni >= h or nj < 0 or nj >= w:
                flag2 = 1
                return
            
            if building[ni][nj] == '#' or building[ni][nj] == '*' or visited[ni][nj]:
                continue
            sanggeun_point.append((ni, nj))
            visited[ni][nj] = 1
            flag = 1
    return flag

t = int(input())

for _ in range(t):
    w, h = map(int, input().split())
    building = [list(input()) for _ in range(h)]
    drow = [-1, 0, 1, 0]
    dcol = [0, 1, 0, -1]
    visited = [[0] * w for _ in range(h)]
    fire_point = deque()
    sanggeun_point = deque()

    for i in range(h):
        for j in range(w):
            if building[i][j] == '*':
                fire_point.append((i, j))
            if building[i][j] == '@':
                sanggeun_point.append((i, j))

    visited[sanggeun_point[0][0]][sanggeun_point[0][1]] = 1
    time = 0
    flag2 = 0

    while True:
        time += 1
        fire()
        for fp in fire_point:
            building[fp[0]][fp[1]] = '*'
        result = escape()
        if flag2:
            print(time)
            break
        if not result:
            print("IMPOSSIBLE")
            break