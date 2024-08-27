# BOJ 1520. 내리막길 > 시간복잡도 해결문제
import sys
input = sys.stdin.readline

def dfs(i, j):
    global cnt

    if i == (m - 1) and j == (n - 1):
        cnt += 1
        return
    
    for k in range(4):
        new_i = i + drow[k]
        new_j = j + dcol[k]

        if 0 <= new_i < m and 0 <= new_j < n and arr[new_i][new_j] < arr[i][j]:
            visited[new_i][new_j] = 1
            dfs(new_i, new_j)
            visited[new_i][new_j] = 0


m, n = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(m)]
cnt = 0

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

visited = [[0] * n for _ in range(m)]
visited[0][0] = 1

dfs(0, 0)
print(cnt)

# def dfs(i, j):
#     if i == M-1 and j == N-1 :  # 목적지에 도착하면, 1 반환
#         return 1

#     if dp[i][j] != -1:          # 방문한 경로라면, 기록된 경로 수 반환
#         return dp[i][j]

#     path_cnt = 0 # 경로 수
#     for k in range(4):
#         ni = i + di[k]
#         nj = j + dj[k]
#         if ni<0 or nj<0 or ni>=M or nj>=N or arr[i][j] <= arr[ni][nj]:
#             continue
#         path_cnt += dfs(ni, nj)

#     dp[i][j] = path_cnt # 경로 수 삽입

#     return dp[i][j]

# M, N = map(int, input().split()) # row / column
# arr = [list(map(int, input().split())) for _ in range(M)]
# di = [0, 1, -1, 0] # right / down / up / left
# dj = [1, 0, 0, -1]
# dp = [[-1] * N for _ in range(M)]   # 초기 경로 값
# print(dfs(0, 0))
# print(dp)