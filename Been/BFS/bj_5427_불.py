# 각 턴 마다의 상근이와 불의 행동을 진행 시켜야 함
# 상근이와 불의 초기 위치를 찾아 초기값 설정 (@ 개수, 첫 턴의 행동 수), 위치 덱에 저장
# 이 때 상근이의 행동이 먼저 작동하도록 덱 맨 앞에 저장
# @ 개수가 0이 되면 탈출 실패
# 덱에서 pop 하면서 상근이와 불의 행동을 현재 행동 수 만큼 진행 (행동 수가 끝나면 턴 +1)
# 상근이의 행동
#  - 델타 탐색으로 빈자리라면 @ 표시, 다음 행동 +1
# 불의 행동
#  - 델타 탐색으로 반자리 or 상근이라면 * 표시, 다음 행동 +1
# 한 턴의 행동이 끝나면 다음 행동을 현재 행동으로 이동, 다음 행동 == 0 처리

from collections import deque


def sg_turn(y, x):
    global turn, sg_cnt, action2
    for k in range(4):
        ni = y + di[k]
        nj = x + dj[k]
        # 빌딩을 벗어나면 탈출 완료
        if ni < 0 or nj < 0 or ni >= h or nj >= w:
            turn += 1
            return 1
        # 빈 공간일 때 다음행동 +, @ 개수 +
        if building[ni][nj] == '.':
            building[ni][nj] = '@'
            queue.append((ni, nj))
            action2 += 1
            sg_cnt += 1
    return 0


def fire_turn(y, x):
    global turn, sg_cnt, action2
    for k in range(4):
        ni = y + di[k]
        nj = x + dj[k]
        if ni < 0 or nj < 0 or ni >= h or nj >= w:
            continue
        # 빈 공간이면 다음행동 +
        if building[ni][nj] == '.':
            building[ni][nj] = '*'
            queue.append((ni, nj))
            action2 += 1
        # 상근이면 다음행동 +, @ 개수 -
        elif building[ni][nj] == '@':
            building[ni][nj] = '*'
            queue.append((ni, nj))
            action2 += 1
            sg_cnt -= 1
            if sg_cnt == 0:
                return 1
    return 0


T = int(input())
for _ in range(T):
    w, h = map(int, input().split())
    building = [list(input().strip()) for _ in range(h)]
    queue = deque([])

    sg_cnt = 1  # @ 개수

    # 한 턴을 표시하기 위한 행동 수
    action = 1  # 현재 행동
    action2 = 0  # 다음 행동

    # @, * 찾아서 행동, 덱에 입력
    for i in range(h):
        for j in range(w):
            if building[i][j] == '@':
                queue.appendleft((i, j))
            elif building[i][j] == '*':
                action += 1
                queue.append((i, j))

    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]
    turn = 0  # 소요 턴(시간)

    # @, *의 행동이 끝날 때 까지
    while queue:
        y, x = queue.popleft()
        action -= 1  # 행동 카운트 -1

        # @ 먼저 행동
        if building[y][x] == '@':
            r = sg_turn(y, x)
            # 탈출 완료하면 종료
            if r == 1:
                print(turn)
                break
        # * 행동
        else:
            f = fire_turn(y, x)
            # 상근이가 탈출 못하면 종료
            if f:
                print('IMPOSSIBLE')
                break

        # 1턴 행동이 완료되면 턴 +
        if action == 0:
            action = action2
            action2 = 0
            turn += 1
    # 행동이 없는데 탈출 못하면 불가능
    else:
        print('IMPOSSIBLE')
