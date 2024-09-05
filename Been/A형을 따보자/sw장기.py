'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?contestProbId=AZGhPln6ymQDFAXd&solveclubId=AZCz7ha6bv8DFAVs&problemBoxTitle=999.+A%ED%98%95%EC%9D%84+%EB%94%B0%EB%B3%B4%EC%9E%90&problemBoxCnt=4&probBoxId=AZGhIDtKx30DFAXd

포가 졸을 먹을 조건을 잘 파악해서 구현해야 했던 문제

포가 3번 움직일 수 있으므로
1. 첫 번째 움직임에는 그냥 이동할 수 있는 곳만 가면 된다 (포를 먹거나 빈 곳이나)
2. 두 번째 부터는 첫 번째에 졸을 먹는 경우와 두 번째에 졸을 먹는 경우도 생각해야한다
   따라서 첫 번째와 두 번째 움직일 때는 왔다 갔다 2번 움직일 수 있으므로 한 칸 더 너머의 졸도 더 먹을 수 있음
   이 경우만 더 세어주면 끝
'''
from collections import deque
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    daek = deque()
 
    a = -1
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                daek.append((i, j, 0))
                visited[i][j] = 2
                break
        if a != -1:
            break
 
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]
 
    ans = 0
    while daek:
        y, x, cnt = daek.popleft()
        for k in range(4):
            tmp = 0
            ni = y + di[k]
            nj = x + dj[k]
            while 0 <= ni < N and 0 <= nj < N:
                if tmp == 0:
                    if arr[ni][nj] == 1:
                        tmp += 1
                        if cnt == 1 and not visited[ni][nj]:
                            drt = (k+2) % 4
                            yi = y + di[drt]
                            xj = x + dj[drt]
                            while 1 <= yi < N - 1 and 1 <= xj < N - 1:
                                if arr[yi][xj] == 1:
                                    visited[ni][nj] = 1
                                    ans += 1
                                    break
                                yi += di[drt]
                                xj += dj[drt]
                    ni += di[k]
                    nj += dj[k]
                elif tmp == 1:
                    if arr[ni][nj] == 1:
                        if not visited[ni][nj]:
                            ans += 1
                        tmp += 1
                        visited[ni][nj] = 1
                        if cnt < 2:
                            daek.append((ni, nj, cnt + 1))
                        ni += di[k]
                        nj += dj[k]
                    else:
                        break

                    print(f'#{tc} {ans}')