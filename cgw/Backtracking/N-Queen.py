def check(col, row):
    for i in range(col):
        if track[i] == row or abs(col-i) == abs(row-track[i]):
            return False
    return True

def nqueen(col):
    global ans
    if col == n:
        ans += 1
        return

    for row in range(n):
        if check(col, row):
            track[col] = row
            nqueen(col+1)

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    track = [0] * n
    ans = 0
    nqueen(0)
    print(f"#{tc} {ans}")