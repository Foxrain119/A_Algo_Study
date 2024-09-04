from collections import deque

di = [-1,1,0,0] # 상하좌우
dj = [0,0,-1,1]

def bfs(sti, stj):
    dq = deque([(sti, stj)])
    area = 1                      # 그림의 넓이

    while dq:
        row, col = dq.popleft()   
        for k in range(4):
            ni = row + di[k]
            nj = col + dj[k]
            if ni<0 or nj<0 or ni>=n or nj>=m or not arr[ni][nj]: # 범위 외이거나, 그림이 없다면
                continue
            arr[ni][nj] = 0       # 검사 완료한 부분은 그림 없애기
            area += 1             # 그림넓이 카운팅
            dq.append((ni, nj))
    return area

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cnt = 0         # 그림의 개수
max_area = 0    # 그림의 최대 넓이

for i in range(n):
    for j in range(m):
        if arr[i][j]:                             # 그림이 있다면
            cnt += 1
            arr[i][j] = 0                         # 검사 완료한 부분은 그림 없애기
            max_area = max(bfs(i, j), max_area)   # 최대 넓이 갱신

print(cnt)
print(max_area)
