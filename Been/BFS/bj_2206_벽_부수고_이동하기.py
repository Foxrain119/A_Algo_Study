'''
https://www.acmicpc.net/problem/2206
'''

from collections import deque
import sys
input = sys.stdin.readline

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]

cost_field = [[[0, 0]for _ in range(M)] for _ in range(N)]
cost_field[0][0] = [1, 1]

lst = deque([(1, 1, 0, 0)])
while lst:
    cost, crush, y, x = lst.popleft()
    if y == N - 1 and x == M - 1:
        print(cost)
        break
    for k in range(4):
        ni = y + di[k]
        nj = x + dj[k]
        if 0 <= ni < N and 0 <= nj < M:
            if crush:
                if arr[ni][nj] == 0 and cost_field[ni][nj][0] == 0:
                    cost_field[ni][nj][0] = cost_field[y][x][0] + 1
                    lst.append((cost_field[ni][nj][0], crush, ni, nj))
                elif arr[ni][nj] == 1 and cost_field[ni][nj][1] == 0:
                    cost_field[ni][nj][1] = cost_field[y][x][0] + 1
                    lst.append((cost_field[ni][nj][1], 0, ni, nj))
            elif arr[ni][nj] == 0 and cost_field[ni][nj][1] == 0:
                cost_field[ni][nj][1] = cost_field[y][x][1] + 1
                lst.append((cost_field[ni][nj][1], crush, ni, nj))
else:
    print(-1)
