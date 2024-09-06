### Study
- [참고블로그](https://blog.encrypted.gg/1035)
- <details>
  <summary>다익스트라 방식1 : for문</summary>

    ```python

      '''
      <input>
      5 6
      1
      5 1 1
      1 2 2
      1 3 3
      2 3 4
      2 4 5
      3 4 6
      '''
      V, E = map(int, input().split()) # 정점, 간선
      st = int(input())

      adj = [[] for _ in range(V + 1)] # 연결된 정점 테이블
      INF = float('inf')
      fix = [0] * (V+1)               # 확정 정점
      d = [[] for _ in range(V+1)]    # 최단거리 테이블

      for _ in range(E):
          d = [INF] * (V + 1)  # 최단 거리 테이블 초기화 / fill(d, d+V+1, INF);
          u, v, w = map(int, input().split())
          adj[u].append((w, v)) # (비용, 간선번호)
          adj[v].append((w, u))

      def dijkstra_naive(st):
          d[st] = 0 # 자기 자신과의 거리는 0
          while True:
              idx = -1 # 가려는 정점 초기화
              for i in range(1, V+1):
                  if fix[i]:           continue # 최단거리 구해진 정점이면 continue
                  if idx == -1:        idx = i
                  elif d[i] < d[idx]:  idx = i

              if idx == -1 or d[idx] == INF: # 더 이상 선택할 정점이 없으면
                  break

              fix[idx] = 1 # 최단거리 구할 정점이므로 사용처리

              for nxtX, nxtY in adj[idx]: # (비용, 간선번호)
                  d[nxtY] = min(d[nxtY], d[idx] + nxtX) # (가려고하는 간선의 현재 가중치) vs (현재간선 가중치+ 다음 간선 가중치)

      dijkstra_naive(st)
      print(d)
    ```
    ```python
      import sys

      inf = float("inf")
      n, m = map(int, sys.stdin.readline().split()) # n: 노드 수, m: 에지 수
      start = int(sys.stdin.readline()) # 시작 노드

      graph = [[] for _ in range(n+1)]
      visited = [False] * (n+1) # 방문 리스트
      dist = [inf] * (n+1) # 거리 리스트

      for _ in range(m): # 그래프 초기화
          v, u, w = map(int, sys.stdin.readline().split())
          graph[v].append((u,w))
      
      def find_smallest_node(): # 거리가 최소인 노드 찾기 
          min_val = inf
          min_idx = 0
          for i in range(1,n+1):
              if not visited[i] and dist[i] < min_val:
                  min_val = dist[i]
                  min_idx = i
          return min_idx

      def dijkstra(start):
          dist[start] = 0
          visited[start] = True
          
          for u, w in graph[start]:
              dist[u] = w
          
          for _ in range(n-1):
              v = find_smallest_node()
              visited[v] = True
              
              for u, w in graph[v]:
                  dist[u] = min(dist[u], dist[v] + w)

      dijkstra(start)
    ```

  </details>

- <details>
  <summary>다익스트라 방식2 : 우선순위 큐</summary>

    ```python
    from heapq import heappush, heappop
    T = int(input())
    for tc in range(1, T+1):
        N, E = map(int, input().split())
        node = [[] for _ in range(N)]
        fix = [float('inf')] * N
        fix[0] = 0 # 시작지점 가중치 0
    
        for _ in range(E):
            a, b, w = map(int, input().split())
            node[a].append((w, b))
    
        h = []
        heappush(h, (0, 0)) # (가중치, 노드번호)
        while h:
            a_w, a_n = heappop(h) # (가중치, 노드번호)
            for b_w, b_n in node[a_n]:
                if a_w + b_w < fix[b_n]:
                    fix[b_n] = a_w + b_w
                    heappush(h, (fix[b_n], b_n))
    
        if fix[N-1] == float('inf'):
            fix[N-1] = 'impossible'
    
        print(f'#{tc} {fix[N-1]}')
    ```

  </details>


### Baekjoon_11404 플로이드 [문제](https://www.acmicpc.net/problem/11404)
- 난이도 : Gold 4
- 알고리즘 : Floyd
- 갈 수 없는 경로 후처리 필요
