### 알고리즘 유형 별 정리

### 시간초과
- 덱에 저장 후, 함수 실행
```python
# 방법1 (비효율)

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            bfs(i, j)

# 방법2 (효율)

from collections import deque
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            dq = deque([(i, j)])

bfs(i, j)
```

- 리스트 직접조회가 아닌, 인덱스로 조회  
```python
# 방법1 (비효율)
for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1]]
    nr = r + dr
    nc = c + dc

# 방법2 (효율)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
for k in range(4)
    nr = r + dr[k]
    nc = c + dc[k]
```

- 백트래킹은 반복 최대 12가 보통

- 함수로 전달하는 인자가 많을수록 오래걸림