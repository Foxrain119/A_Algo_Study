t = int(input())

# dfs로 접근하는 것과 bfs로 접근하는 것의 차이가 있는 문제일까??
def dfs(node):
    for nod in adj_lst[node]:
        if not visited[nod]:
            visited[nod] = 1
            dfs(nod)

for tc in range(1, t + 1):
    n, m = map(int, input().split())
    adj_lst = [[] for _ in range(n + 1)]
    # 양방향 인접리스트 생성
    for _ in range(m):
        x, y = map(int, input().split())
        adj_lst[x].append(y)
        adj_lst[y].append(x)
    visited = [0] * (n + 1)
    cnt = 0

    for i in range(1, n + 1): # 각각의 마을에서 탐색해보자 -> 그래프가 끊겨 있을 테니깐
        if not visited[i]: # 방문한 적이 없다면 탐색
            visited[i] = 1
            dfs(i)
            cnt += 1
    
    print(f'#{tc} {cnt}')