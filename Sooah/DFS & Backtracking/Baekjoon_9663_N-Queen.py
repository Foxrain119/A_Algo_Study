def check(new_queen_row, new_col):
    for before_queen_row in range(new_queen_row): # 이전 퀸 검사
        if new_col == chess[before_queen_row] or abs(new_col - chess[before_queen_row]) == abs(new_queen_row - before_queen_row): # 이미 방문한 열이거나, 열간격과 행간격이 같다면
            return False
    return True

def back(queen_row):
    global ans

    if queen_row == N:
        ans += 1
        return

    for col in range(N):
        if check(queen_row, col):
            chess[queen_row] = col
            back(queen_row + 1)

N = int(sys.stdin.readline())
chess = [-1] * N  # chess[행이자 퀸 번호] = 열 / 채워져있으면 퀸이 있는 것

ans = 0
back(0)           # 퀸 개수

print(ans)