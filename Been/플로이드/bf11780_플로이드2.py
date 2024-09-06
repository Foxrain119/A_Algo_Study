'''
https://www.acmicpc.net/problem/11780
플로이드2
'''
n = int(input())
m = int(input())
arr = [[0] * n for _ in range(n)]
nxt = [[0] * n for _ in range(n)]

for _ in range(m):
    y, x, k = map(int, input().split())
    nxt[y - 1][x - 1] = x - 1
    if arr[y - 1][x - 1]:
        arr[y - 1][x - 1] = min(arr[y - 1][x - 1], k)
    else:
        arr[y - 1][x - 1] = k

for k in range(n):
    for i in range(n):
        for j in range(n):
            # 이동이 아닌 경우 제외
            if i == j or i == k or j == k:
                continue
            # 중간 노선이 이어지지 않는 경우 제외
            if arr[i][k] == 0 or arr[k][j] == 0:
                continue
            # 가상 노선 비용 (거쳐서 이동하는 노선)
            if arr[i][j] == 0:
                arr[i][j] = arr[i][k] + arr[k][j]
                if nxt[i][k] != k:
                    nxt[i][j] = nxt[i][k]
                    continue
                nxt[i][j] = k
            elif arr[i][j] > arr[i][k] + arr[k][j]:
                arr[i][j] = arr[i][k] + arr[k][j]
                if nxt[i][k] != k:
                    nxt[i][j] = nxt[i][k]
                    continue
                nxt[i][j] = k

for i in range(n):
    print(*arr[i])

for i in range(n):
    for j in range(n):
        if arr[i][j]:
            ni = i
            tmp = [i + 1, nxt[i][j] + 1]
            while nxt[ni][j] != j:
                ni = nxt[ni][j]
                tmp.append(nxt[ni][j] + 1)
            print(len(tmp), *tmp)
        else:
            print(0)
for i in range(n):
    print(*nxt[i])