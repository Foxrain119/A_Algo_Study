'''
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV597vbqAH0DFAVl

미생물들의 행동들을 '동시에' 진행해야 되는게 핵심인 문제

1. 군집의 정보를 받고 (개수, 방향)을 새겨주면서 덱에 좌표 추가

2. 같은 크기에 다른 군집을 생성(visited), 3개가 같은 곳에 뭉칠 때 뭉치기 전의 큰 개수 값과 방향을 저장하기 위해 체킹 배열 생성 (count)
   1턴을 끊어주기 위해! 현재 진행할 행동 수(move1), 다음에 진행할 행동 수(move2), 군집을 스위칭할 변수(switch : 0 or 1) 을 변수로 생성

3. 1턴 진행하면서 다른 군집에 (개수, 방향)을 새겨주고 좌표를 덱에 추가
   이미 새겨져 있는데 처음 뭉치는 경우 체킹 배열(count)에 뭉치기 전 [큰 값, 방향] 저장
   3번째 뭉치는 경우 체킹 배열(count)에 저장된 값과 비교하여 군집과 체킹 배열에 새김
   뭉치지 않는 경우 다음 행동 개수 + 1

4. 1턴이 끝나면
   진행 시간 - 1
   현재 행동 업데이트 (다음 행동 가져옴)
   다음 행동 == 0
   새겨진 군집 반대군집 0으로 초기화 (새로 새겨야 되니까)
   군집 스위칭해줌

'''
from collections import deque

# 상하좌우
di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, -1, 1]
T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = [[0] * N for _ in range(N)]
    deq = deque()
    visited = [[0] * N for _ in range(N)]
    count = [[0] * N for _ in range(N)]
    switch = 0  # 판 바꾸기
    move1 = K  # 현재 행동
    move2 = 0  # 다음 행동
    for _ in range(K):
        y, x, n, k = map(int, input().split())
        arr[y][x] = [n, k]
        deq.append([y, x])

    # 행동
    while M:
        # 1턴
        if switch == 0:
            place = visited
            other_place = arr
        else:
            place = arr
            other_place = visited

        for _ in range(move1):
            yi, xj = deq.popleft()
            num, drt = other_place[yi][xj]
            ni = yi + di[drt]
            nj = xj + dj[drt]
            if 0 < ni < N - 1 and 0 < nj < N - 1:
                if place[ni][nj] == 0:
                    place[ni][nj] = [num, drt]
                    deq.append([ni, nj])
                    move2 += 1
                # 2개 겹칠 경우
                elif not count[ni][nj]:
                    if place[ni][nj][0] > num:
                        count[ni][nj] = [place[ni][nj][0], place[ni][nj][1]]
                        # print(count)
                        place[ni][nj][0] += num
                        # print(count)
                    else:
                        place[ni][nj][0] += num
                        place[ni][nj][1] = drt
                        count[ni][nj] = [num, drt]
                # 3개 이상 겹칠 경우
                else:
                    if count[ni][nj][0] > num:
                        place[ni][nj][0] += num
                    else:
                        place[ni][nj][0] += num
                        place[ni][nj][1] = drt
                        count[ni][nj] = [num, drt]

            elif ni == 0 or nj == 0 or ni == N - 1 or nj == N - 1:
                if drt % 2 == 1:
                    drt += 1
                else:
                    drt -= 1
                place[ni][nj] = [num//2, drt]
                deq.append([ni, nj])
                move2 += 1

        # 판 갈기
        if switch == 0:
            arr = [[0] * N for _ in range(N)]
        else:
            visited = [[0] * N for _ in range(N)]
        count = [[0] * N for _ in range(N)]

        switch = (switch + 1) % 2
        # 현재 행동 갱신
        move1 = move2
        move2 = 0

        M -= 1

    if switch == 0:
        now = arr
    else:
        now = visited

    result = 0
    for i in range(N):
        for j in range(N):
            if now[i][j]:
                result += now[i][j][0]

    print(f'#{tc} {result}')













