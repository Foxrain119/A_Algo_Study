### 유니온파인드 Process
1. 부모테이블을 자기자신으로 초기화
2. 두 원소가 속한 집한 합치기
  - 루트노드를 재귀적으로 찾아서, 부모노드 갱신
    ```python
      def find_parent(x):
          if parent[x] != x:
              parent[x] = find_parent(parent[x])
          return parent[x]
    ```

3. 각 원소가 속한 집합 == 부모테이블의 값


### Baekjoon_1976 여행 가자 [문제](https://www.acmicpc.net/problem/1976)  
- 난이도 : Gold 4
- 알고리즘 : 유니온파인드
