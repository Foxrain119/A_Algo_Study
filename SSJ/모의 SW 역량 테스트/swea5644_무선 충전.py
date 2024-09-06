# grid에 performance 값을 넣으면 풀 수가 없다.
# 반례 ) [0, 350, 350, 350], [0, 350]
# 따라서 grid에 battery charger의 고유 번호를 넣어주고, dictionary를 활용한다.

from collections import deque

def distance(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)

def whatismax(lst): # 특정 grid 내에서 최대 performance를 출력하는 함수
    tmp = 0
    tmp_idx = -1
    for ls in lst:
        if bc[ls] > tmp:
            tmp = bc[ls]
            tmp_idx = ls
    return (tmp, tmp_idx)

def whatisrealmax(lst1, lst2): # bc 영역이 겹칠 때 performance 합의 최대값을 출력하는 함수 -> lst1 : [0, 20, 40], lst2 : [0, 40]
    tmp1 = whatismax(lst1)
    tmp2 = 0
    for x in lst2:
        if bc[x] > tmp2 and x != tmp1[1]: 
            tmp2 = bc[x]

    tmp3 = whatismax(lst2)
    tmp4 = 0
    for y in lst1:
        if bc[y] > tmp4 and y != tmp3[1]:
            tmp4 = bc[y]
    
    return max(tmp1[0] + tmp2, tmp3[0] + tmp4)

t = int(input())

for tc in range(1, t + 1):
    m, a = map(int, input().split())
    moving_a = deque(list(map(int, input().split())))
    moving_b = deque(list(map(int, input().split())))
    grid = [[[] for _ in range(10)] for _ in range(10)]

    bc = {}
    for bcnum in range(a):
        bc_j, bc_i, c_range, perfor = map(int, input().split())
        bc[bcnum] = perfor # 각각의 battery charger의 고유값을 키로, performance를 값으로 넣어준다.
        for i in range(10):
            for j in range(10):
                if distance(bc_i - 1, bc_j - 1, i, j) <= c_range:
                    grid[i][j].append(bcnum) # battery charger의 고유값을 넣어준다.

    a_now_i, a_now_j = 0, 0
    b_now_i, b_now_j = 9, 9

    drow = [0, -1, 0, 1, 0]
    dcol = [0, 0, 1, 0, -1]

    answer = 0
    for asdf in range(m + 1):
        if asdf > 0:
            pop_ma = moving_a.popleft()
            a_now_i += drow[pop_ma]
            a_now_j += dcol[pop_ma]

            pop_mb = moving_b.popleft()
            b_now_i += drow[pop_mb]
            b_now_j += dcol[pop_mb]

        if set(grid[a_now_i][a_now_j]).intersection(set(grid[b_now_i][b_now_j])):
            if len(grid[a_now_i][a_now_j]) == 1 and len(grid[b_now_i][b_now_j]) == 1: # 사용자 A, B 둘 다 겹치는 한 영역위에 있을 경우 -> 한 영역의 performance 값을 더해준다.
                answer += whatismax(grid[a_now_i][a_now_j])[0]
            else:
                answer += whatisrealmax(grid[a_now_i][a_now_j], grid[b_now_i][b_now_j])
        else:
            answer += (whatismax(grid[a_now_i][a_now_j])[0] + whatismax(grid[b_now_i][b_now_j])[0])

    print(f'#{tc} {answer}')