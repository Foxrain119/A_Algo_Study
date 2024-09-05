'''
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5VwAr6APYDFAWu

BFS 든 DFS 든 상관없이
돌릴 때 방향을 제한해주고 사각형을 만들 수 없는 조건은 쳐내주는 문제

1. 나는 우하단, 좌하단, 좌상단, 우상단(이후 1, 2, 3, 4 방향으로 명함) 으로 사각형이 만들어지도록 제한
2. 행의 맨 아래 2줄은 사각형을 만들 수 없음
   마찬가지로 열의 양 옆 끝 2줄은 사각형을 만들 수 없음
   이 안의 모든 점에서 사각형 그리기를 시작
   이동하면서 디저트를 리스트에 저장하면서 이동 (겹치는 걸 확인하기 위해)
3. 사각형이 그려지면  1과 3 방향 2와 4 방향의 길이는 같아야 사각형이다.
   따라서 1, 2를 이동한 횟수를 변수로 만들어 이동할 때 마다 + 1
   3, 4를 이동할 때는 각 변수 - 1 하여 0이 되면 사각형이 완성
4. 하지만 나는 다음으로 이동했을 경우를 탐색하기에
   우상단으로 갈 때 출발지 바로 앞에서 멈추게 해야 사각형 완성이 된다.
   따라서 4로 이동할 때 1이 남을 때 스탑하도록 설정
5. 가지치기한 조건은
    1) 1방향으로 1칸도 안 움직였을 경우
    2) 디저트가 겹친 경우
    3) 1, 2로 이동한 횟수를 3,4 이동이 벗어날 때

쓸데없이 길게 짠 코드...
더 최적화 해야되지만 그건 귀찮다
'''
from collections import deque

di = [1, 1, -1, -1]
dj = [1, -1, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    deq = deque()

    ans = -1
    for i in range(N - 2):
        for j in range(1, N - 1):
            drt = 0
            deq.append([i, j, 0, 0, 0, [arr[i][j]]])  # 좌표, 우하대각 길이, 좌하대각 길이, 방향

            while deq:
                y, x, r, l, drt, dessert = deq.popleft()
                if drt == 3 and l == 1:
                    if ans < len(dessert):
                        ans = len(dessert)
                        # print(y, x, dessert)
                        continue
                if drt == 0:
                    ni1 = y + di[drt]
                    nj1 = x + dj[drt]
                    ni2 = y + di[drt + 1]
                    nj2 = x + dj[drt + 1]
                    if 0 <= ni1 < N and 0 <= nj1 < N and arr[ni1][nj1] not in dessert:
                        deq.append([ni1, nj1, r + 1, l, drt, dessert + [arr[ni1][nj1]]])
                    if N > ni2 >= 0 != r and 0 <= nj2 < N and arr[ni2][nj2] not in dessert:
                        deq.append([ni2, nj2, r, l + 1, drt + 1, dessert + [arr[ni2][nj2]]])

                elif drt == 1:
                    ni1 = y + di[drt]
                    nj1 = x + dj[drt]
                    ni2 = y + di[drt + 1]
                    nj2 = x + dj[drt + 1]
                    if 0 <= ni1 < N and 0 <= nj1 < N and arr[ni1][nj1] not in dessert:
                        deq.append([ni1, nj1, r, l + 1, drt, dessert + [arr[ni1][nj1]]])
                    if N > ni2 >= 0 and 0 <= nj2 < N and arr[ni2][nj2] not in dessert:
                        deq.append([ni2, nj2, r - 1, l, drt + 1, dessert + [arr[ni2][nj2]]])

                elif drt == 2:
                    ni1 = y + di[drt]
                    nj1 = x + dj[drt]
                    ni2 = y + di[drt + 1]
                    nj2 = x + dj[drt + 1]
                    if r != 0 <= ni1 < N and 0 <= nj1 < N and arr[ni1][nj1] not in dessert:
                        deq.append([ni1, nj1, r - 1, l, drt, dessert + [arr[ni1][nj1]]])
                    if N > ni2 >= 0 and 0 <= nj2 < N:
                        if r == 0 and l == 1:
                            if ans < len(dessert):
                                ans = len(dessert)
                        elif r == 0 and arr[ni2][nj2] not in dessert:
                            deq.append([ni2, nj2, r, l - 1, drt + 1, dessert + [arr[ni2][nj2]]])
                elif drt == 3:
                    ni1 = y + di[drt]
                    nj1 = x + dj[drt]
                    if l != 0 <= ni1 < N and 0 <= nj1 < N and arr[ni1][nj1] not in dessert:
                        deq.append([ni1, nj1, r, l - 1, drt, dessert + [arr[ni1][nj1]]])
    print(f'#{tc} {ans}')