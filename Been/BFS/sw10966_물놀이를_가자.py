'''
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXWXMZta-PsDFAST&categoryId=AXWXMZta-PsDFAST&categoryType=CODE&problemTitle=%EB%AC%BC%EB%86%80%EC%9D%B4&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

이상한 문제 ㅡㅡ
수영장에서 'L' 을 숫자로 바꾸는게 pypy 에서 캐시를 삭제하고 재추출 하는데 문제가 조금 발생하는 듯
visited 로 접근하면 풀리는 이상한 문제
'''
from collections import deque


def bfs():
    ans = 0
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    deq = deque()

    for i in range(N):
        for j in range(M):
            if pool[i][j] == 'W':
                deq.append((1, i, j))
                visited[i][j] = 0

    while deq:
        time, x, y = deq.popleft()
        for k in range(4):
            ni = x + di[k]
            nj = y + dj[k]
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == -1:
                ans += time
                visited[ni][nj] = 1
                deq.append((time + 1, ni, nj))
    return ans


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    pool = [input() for _ in range(N)]
    visited = [[-1] * M for _ in range(N)]

    result = bfs()
    print(f'#{tc} {result}')
