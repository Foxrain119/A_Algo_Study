'''
https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AZIyCYJ6p30DFAQP
'''
from collections import deque
from heapq import heappop, heappush

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    visited = [[[0 for _ in range(K + 1)]for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'X':
                start = (i, j)
            elif arr[i][j] == 'Y':
                end = (i, j)

    print(f'#{tc}', end=' ')
    # dq = deque([(0, K - 1, start[0], start[1], 0)])
    hq = [(0, K, start[0], start[1], 0)]
    while hq:
        cost, tree, y, x, drt = heappop(hq)
        if visited[y][x][tree] != 0 and visited[y][x][tree] <= cost:
            continue
        visited[y][x][tree] = cost
        # cost, tree, y, x, drt = dq.popleft()
        if y == end[0] and x == end[1]:
            print(cost)
            break
        nxt = cost + 1
        # if drt == 0:
        #     # heappush(hq, (nxt, tree, y, x, 3))
        #     dq.append((nxt, tree, y, x, 3))
        # else:
        #     # heappush(hq, (nxt, tree, y, x, drt - 1))
        #     dq.append((nxt, tree, y, x, drt - 1))
        #
        # if drt == 3:
        #     # heappush(hq, (nxt, tree, y, x, 0))
        #     dq.append((nxt, tree, y, x, 0))
        # else:
        #     # heappush(hq, (nxt, tree, y, x, drt + 1))
        #     dq.append((nxt, tree, y, x, drt + 1))
        for k in range(4):
            ni = y + di[k]
            nj = x + dj[k]
            nk = abs(drt - k)
            if 0 <= ni < N and 0 <= nj < N:
                # 갈 수 있는 길
                if (arr[ni][nj] == 'G' or arr[ni][nj] == 'Y') and visited[ni][nj][tree] == 0:
                    if nk == 0:
                        # visited[ni][nj][tree] = nxt
                        heappush(hq, (nxt, tree, ni, nj, drt))
                    elif nk == 2:
                        # visited[ni][nj][tree] = nxt + 2
                        heappush(hq, (nxt + 2, tree, ni, nj, k))
                    else:
                        # visited[ni][nj][tree] = nxt + 1
                        heappush(hq, (nxt + 1, tree, ni, nj, k))
                # 나무
                elif arr[ni][nj] == 'T' and tree > 0 and visited[ni][nj][tree - 1] == 0:
                    if nk == 0:
                        # visited[ni][nj][tree - 1] = nxt
                        heappush(hq, (nxt, tree - 1, ni, nj, drt))
                    elif nk == 2:
                        # visited[ni][nj][tree - 1] = nxt + 2
                        heappush(hq, (nxt + 2, tree - 1, ni, nj, k))
                    else:
                        # visited[ni][nj][tree - 1] = nxt + 1
                        heappush(hq, (nxt + 1, tree - 1, ni, nj, k))

        # ni = y + di[drt]
        # nj = x + dj[drt]
        # if 0 <= ni < N and 0 <= nj < N:
        #     if arr[ni][nj] == 'G' and visited[ni][nj][tree] == 0:
        #         visited[ni][nj][tree] = nxt
        #         # heappush(hq, (nxt, tree, ni, nj, drt))
        #         dq.append((nxt, tree, ni, nj, drt))
        #
        #     elif arr[ni][nj] == 'T' and tree > 0 and visited[ni][nj][tree - 1] == 0:
        #         visited[ni][nj][tree - 1] = nxt
        #         # heappush(hq, (nxt, tree - 1, ni, nj, drt))
        #         dq.append((nxt, tree - 1, ni, nj, drt))
        #     elif arr[ni][nj] == 'Y':
        #         print(cost + 1)
        #         break
    else:
        print(-1)
