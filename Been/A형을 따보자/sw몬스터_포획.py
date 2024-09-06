'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?contestProbId=AZGhS4yay-4DFAXd&solveclubId=AZCz7ha6bv8DFAVs&problemBoxTitle=999.+A%ED%98%95%EC%9D%84+%EB%94%B0%EB%B3%B4%EC%9E%90&problemBoxCnt=4&probBoxId=AZGhIDtKx30DFAXd

BFS 같지만 BFS 가 아닌 문제

출발점과 몬스터, 의뢰자 각각의 위치에서
서로 떨어진 거리(시간)을 조합으로 조건을 추가해서 최소값을 되하면 된다.
몬스터를 먹어야 의뢰자에게 갈 수 있으므로 의뢰자를 먼저 추가하는 경우를 쳐내면 된다.
'''


from collections import deque


def comb(count):
    global cnt, result
    # 종료 조건
    if count == cnt + 1:
        tmp = 0
        for i in range(cnt):
            y, x = subdeq[i], subdeq[i+1]
            tmp += graph[y][x]
        if result > tmp:
            result = tmp
            return

    for i in range(cnt + 1):
        if not visited[i]:
            if i < cnt//2 and not visited[cnt - i]:
                continue
            subdeq.append(i)
            visited[i] = 1
            comb(count + 1)
            subdeq.pop()
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 의뢰 개수
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                cnt += 1
    # 위치
    pos = [0] * (cnt + 1)
    pos[cnt//2] = (0, 0)
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                pos[arr[i][j] + (cnt//2)] = (i, j)
    # 소요 시간
    graph = [[0] * (cnt + 1) for _ in range(cnt + 1)]
    for i in range(cnt + 1):
        for j in range(cnt + 1):
            if i == j:
                continue
            graph[i][j] = abs(pos[i][0] - pos[j][0]) + abs(pos[i][1] - pos[j][1])

    target = list(range(-(cnt//2), (cnt//2) + 1))
    visited = [0] * (cnt + 1)
    visited[cnt//2] = 1
    result = 99999
    subdeq = deque([cnt//2])

    comb(1)
    print(f'#{tc} {result}')