from collections import deque

def backtrack(row, col, type):
    global cnt, time
    dq = deque([(row, col, type)])
    visited[row][col] = 1
    cnt += 1 # 맨홀 뚜껑은 무조건 방문하니깐!
    time += 1 # 맨홀 뚜껑으로 입장할 때 시간 1 사용
    while dq:
        if time == l:
            return
        
        for i in range(len(dq)): # 과정 한 번 사용(== 시간 1 사용)
            prow, pcol, ptype = dq.popleft()
            for j in range(len(d_dict[ptype])):
                nrow = prow + d_dict[ptype][j][0]
                ncol = pcol + d_dict[ptype][j][1]

                if nrow < 0 or nrow >= n or ncol < 0 or ncol >= m or visited[nrow][ncol]:
                    continue

                if grid[nrow][ncol] == 0:
                    continue

                if d_dict[ptype][j][0] == -1 and d_dict[ptype][j][1] == 0 and grid[nrow][ncol] in {3, 4, 7}: # 위로 이동할 건데 못가는 경우라면?
                    continue
                
                if d_dict[ptype][j][0] == 0 and d_dict[ptype][j][1] == 1 and grid[nrow][ncol] in {2, 4, 5}: # 오른쪽으로 이동할 건데 못가는 경우라면?
                    continue

                if d_dict[ptype][j][0] == 1 and d_dict[ptype][j][1] == 0 and grid[nrow][ncol] in {3, 5, 6}: # 아래로 이동할 건데 못가는 경우라면?
                    continue

                if d_dict[ptype][j][0] == 0 and d_dict[ptype][j][1] == -1 and grid[nrow][ncol] in {2, 6, 7}: # 왼쪽으로 이동할 건데 못가는 경우라면?
                    continue
                
                visited[nrow][ncol] = 1
                cnt += 1
                dq.append((nrow, ncol, grid[nrow][ncol]))
                
        time += 1

t = int(input())

for tc in range(1, t + 1):
    n, m, r, c, l = map(int, input().split()) # 지도 세로 길이, 지도 가로길이, 뚜껑 세로 위치, 뚜껑 가로 위치, 탈출 후 소요된 시간  
    grid = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    time = 0
    cnt = 0
    # 구조물의 종류에 따라 내가 가야할 방향은 정해져 있다
    # 구조물의 고유 번호가 grid 안에 있으니 딕셔너리로 dxy(delta row column)을 지정해준다.
    d_dict = {1 : [(-1, 0), (0, 1), (1, 0), (0, -1)], 2 : [(-1, 0), (1, 0)], 
              3 : [(0, 1), (0, -1)], 4 : [(-1, 0), (0, 1)], 5 : [(1, 0), (0, 1)], 
              6 : [(1, 0), (0, -1)], 7 : [(-1, 0), (0, -1)]}

    backtrack(r, c, grid[r][c])
    print(f'#{tc} {cnt}')