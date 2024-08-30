import sys
from collections import deque
dr = [-1, 1, 0, 0] # up down right left
dc = [0, 0, 1, -1]
input = sys.stdin.readline

def back(sti, stj, sec):          # (시작행, 시작열, 현재 시간)
    dq = deque([(sti, stj, sec)])
    time_arr[sti][stj] = 0        # 시작위치의 시간 = 0
    while dq:
        x, y, time = dq.popleft()
        for k in range(4):              # 4방향 검사
            for power in range(1, K+1): # 최대 K만큼 이동 
                ni = x + dr[k] * power
                nj = y + dc[k] * power
                if ni < 0 or nj < 0 or ni >= N or nj >= M or arr[ni][nj] == '#': # 범위 벗어나거나, 벽인 경우 다른 방향 탐색
                    break
                if -1 < time_arr[ni][nj] < time: # 이미 저장된 시간이 현재 시간보다 작으면, 고려할 필요x
                    break
                if -1 < time_arr[ni][nj]:        # 이미 저장된 시간이 현재 시간보다 크거나 같으면, 같은 방향 다음 칸 검사
                    continue
                time_arr[ni][nj] = time          # 현재 시간 저장
                dq.append((ni, nj, time + 1))


N, M, K = map(int, input().split())               # N x M: 체육관크기 / K: 초당 최대 이동 칸
arr = [list(input().strip()) for _ in range(N)]   # 체육관
time_arr = [[-1]*M for _ in range(N)]             # 시간 값 저장용
x1, y1, x2, y2 = map(int, input().split())

back(x1-1, y1-1, 1)                               # 첫째 줄이 1번(index=0)으로 시작

print(time_arr[x2-1][y2-1])