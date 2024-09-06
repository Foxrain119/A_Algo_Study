'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZCz7ha6bv8DFAVs&contestProbId=AZGhGOJqxrUDFAXd&probBoxId=AZGhIDtKx30DFAXd&type=USER&problemBoxTitle=999.+A%ED%98%95%EC%9D%84+%EB%94%B0%EB%B3%B4%EC%9E%90&problemBoxCnt=4

각 목적지 마다 출발지에서의 4분면을 따져 꺾어야 하는 횟수를 구해 더해주면 되는 문제


근데 나는 꺾은 횟수를 key로 하는 최소 힙을 사용해 최종목적지까지의 가장 적은 회전 횟수를 구함
그걸 위해 힙에 (꺾은 횟수, 목적지의 도착한 횟수, 행, 열, 방향)을 요소로 넣어줬다.

또한 더 꺾은 경우를 제하기 위해, 각 목적지에 도달할 때마다 도착한 목적지 번호와 도착할 때 까지 꺾은 횟수를 변수로 기록
도착이 같거나 적은데 많이 꺾었을 때 continue
'''
from heapq import heappush, heappop
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 꺾은 횟수, 먹은 개수, 행, 열, 방향
    hq = [[0, 0, 0, 0, 0]]

    apple = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                apple += 1
    ans = 0
    a_point = 0
    c_point = 99
    while hq:
        cnt, apples, y, x, drt = heappop(hq)
        if apples == apple:
            ans = cnt
            break
        # 사과 갯수가 적은데 꺾은 횟수가 같거나 많을 때
        if a_point > apples and c_point <= cnt:
            continue

        ni = y + di[drt]
        nj = x + dj[drt]
        if 0 <= ni < N and 0 <= nj < N:
            if arr[ni][nj] == apples + 1:
                heappush(hq, (cnt, apples + 1, ni, nj, drt))
                a_point = arr[ni][nj]
                c_point = cnt
                continue
            else:
                heappush(hq, (cnt, apples, ni, nj, drt))

        drt2 = (drt + 1) % 4
        nni = y + di[drt2]
        nnj = x + dj[drt2]
        if 0 <= nni < N and 0 <= nnj < N:
            heappush(hq, (cnt + 1, apples, y, x, drt2))

    print(f'#{tc} {ans}')