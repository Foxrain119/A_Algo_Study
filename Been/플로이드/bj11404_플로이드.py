'''
https://www.acmicpc.net/problem/11404
플로이드
'''
# 정점 개수
n = int(input())
# 노선 개수
m = int(input())

# 최단 거리 테이블
arr = [[0] * n for _ in range(n)]
for _ in range(m):
    y, x, k = map(int, input().split())
    if arr[y - 1][x - 1]:
        arr[y - 1][x - 1] = min(arr[y - 1][x - 1], k)
    else:
        arr[y - 1][x - 1] = k

# 최단 거리 갱신
for k in range(n):  # n번 정점을 거쳐가는
    for i in range(n):  # 출발 정점
        for j in range(n):  # 도착 정점
            # 출발 도착이 같으면 이동하는게 아님
            if i == j or i == k or j == k:
                continue
            # 거쳐갈 수 없으면 패스
            if arr[i][k] == 0 or arr[k][j] == 0:
                continue

            # 테이블 갱신
            if arr[i][j] == 0:  # 노선이 없는 경우
                arr[i][j] = arr[i][k] + arr[k][j]
            else:  # 노선이 있지만 돌아가는게 더 빠를 경우 갱신
                arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

for i in range(n):
    print(*arr[i])
