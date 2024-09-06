# 좌하향 -> 우하향 -> 우상향으로 사각형을 만들면 되지!!
# 예전에 오목, 오셀로를 떠올려보자 -> grid 위에서부터 아래로 차례차례 탐색한다면 위의 방법대로 해도 상관이 없다.

def backtrack(row, col, trans, include): # 현재 행 인덱스, 현재 열 인덱스, 꺾은 횟수, 지나온 가게
    global answer # 가게 수를 담는 변수

    if row == start_i and col == start_j and trans == 3: # 현재 행, 열 인덱스와 시작점의 행, 열 인덱스가 같다면 종료해주고, answer 변수를 갱신
        answer = max(answer, len(include))
        return
    
    if trans > 3: # 네 번 이상 꺾었다면 종료
        return
    
    if row < 0 or row >= n or col < 0 or col >= n: # 현재 행, 열 인덱스가 grid 범위 밖이면
        return
    
    if grid[row][col] in include: # 현재 가게를 이미 지나왔다면
        return

# --------------------------------------------------------------------------------

    include.append(grid[row][col]) # 현재 가게를 include 리스트에 넣어준다
    nrow = row + dxy[trans][0] # 변화 해서 온 값 -> 어려워...
    ncol = col + dxy[trans][1] # 변화 해서 온 값 -> 어려워...

    backtrack(nrow, ncol, trans, include) # 이전에 온 방향으로 ㄱㄱ
    if trans < 3:
        backtrack(nrow, ncol, trans + 1, include) # 세 번 미만으로 꺾었다면 꺾어
        
    include.pop()
        
# ----------------------------------------------------------------------------------

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    dxy = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
    answer = -1

    # grid의 n - 2번, n - 1번 인덱스의 행과 0번, n - 1번 인덱스의 열은 시작점이 될 수 없다.
    for i in range(n - 2):
        for j in range(1, n - 1):
            start_i, start_j = i, j
            backtrack(start_i, start_j, 0, []) # 리스트를 인자로 받아주는 방법!!!
    
    print(f'#{tc} {answer}')