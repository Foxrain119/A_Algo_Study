def backtracking(key): # key는 행의 인덱스를 나타낸다.
    global cnt
 
    if key == n: # key가 n이라면 모든 행에 퀸이 하나씩 놓인 것이므로 종료
        cnt += 1
        return
     
    for i in range(n): # i는 해당 행에서 열의 인덱스를 의미한다.
        for j in range(key): # 이전에 놓인 퀸들로 인해 놓는데 제한되는 열, 좌대각, 우대각 조건
            if i == visited[j] or i == (j + visited[j] - key) or i == (key + visited[j] - j):
                break
        else:
            visited[key] = i
            backtracking(key + 1)
            visited[key] = -1
 
t = int(input())
 
for tc in range(1, t + 1):
    n = int(input())
    # grid = [[0] * n for _ in range(n)]
    visited = [-1] * n
    cnt = 0
     
    backtracking(0)
 
    print(f'#{tc} {cnt}')