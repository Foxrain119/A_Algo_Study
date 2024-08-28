'''
불 번짐과 이동하는 경우를 구분하는 것이 중요
'''

from collections import deque

# 시작 위치 찾기
def find_st():
    for i in range(h):
        for j in range(w):
            if arr[i][j] == '@':
                return i, j

# 불 번짐
def fire():
    global fire_li
    tmp_li = deque([])
    while fire_li:
        firei, firej = fire_li.popleft()
        for k in range(4):
            nfi = firei + di[k]
            nfj = firej + dj[k]
            if nfi < 0 or nfj < 0 or nfi >= h or nfj >= w or arr[nfi][nfj] == '#' or arr[nfi][nfj] == '*':
                continue
            arr[nfi][nfj] = '*'
            tmp_li.append((nfi, nfj))

    fire_li = deque([])
    for data in tmp_li:
        fire_li.append(data)

# 1초간 이동
def bfs():
    global ans
    tmp_dq = deque([])
    while dq:
        nowi, nowj, time = dq.popleft()           # 행, 열, 시간
        for k in range(4):
            ni = nowi + di[k]
            nj = nowj + dj[k]

            if ni<0 or nj<0 or ni>=h or nj>=w:   # 탈출한 경우, 시간 반환
                return time

            if arr[ni][nj] == '.':
                arr[ni][nj] = '#'                # 이동한 지점 못 가게 벽(#)으로 처리 (visited와 동일하게 작동)
                tmp_dq.append((ni, nj, time+1))  # 1초 동안 이동한 지점 저장
              
    for data in tmp_dq:
        dq.append(data)                          # 다음 이동 위한 이동하는 지점 업데이트
      
    return 1000000                               # 탈출 못한 경우, 초기값 반환


di = [-1, 1, 0, 0] # 상하좌우
dj = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    ans = 1000000
    w, h = map(int, input().split())
    arr = [list(input()) for _ in range(h)]
  
    fire_li = deque([])                     # 처음 불이 있는 위치
    for i in range(h):
        for j in range(w):
            if arr[i][j] == '*':
                fire_li.append((i, j))

    sti, stj = find_st()                    # 시작 위치
    dq = deque([(sti, stj, 1)])

    while dq:
        fire()                              # 불 번짐
        res = bfs()                         # 이동
        if res != 1000000:
            ans = min(ans, res)             # 최소 시간 갱신

    if ans == 1000000:                      # 모든 이동을 완료한 후에 ans가 초기값이면,
        ans = 'IMPOSSIBLE'

    print(ans)
