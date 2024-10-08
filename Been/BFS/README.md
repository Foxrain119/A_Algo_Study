1. (실1) 백준 1926 그림
   -
   - 전체 N x M 을 탐색하면서, 방문 안 한 지점이면 bfs 함수 실행
   - bfs 함수로 섬 넓이 도출

2. (골4) 백준 5427 불
   -
   - 사람과 불을 한 턴으로 묶어 행동을 진행시켜야 하는 문제였음
   - 턴을 정해줘야 하기에 체크하는 변수가 많았음 (턴 수, 현재 행동, 다음 행동, 사람 수)
   - 덱을 활용해서 popleft 로 사람 먼저 행동한 후 불 행동을 진행 (사람 먼저 행동했으니 먼저 append 되어 있고 다음 행동에서도 사람 먼저 행동할 수 있음)
   - 나머지 사람이 벽에 갇힌 경우 불가 처리해주면서 완료

3. (플3) 백준 16903 달리기
   - BFS 지만 한번에 여러 칸 수를 갈 수 있어서 BFS 를 진행하는 순서를 잘 정돈하는게 어려웠다.
   - 처음에는 우선순위를 정해주기 위해 최소heap 을 사용하여 시간 순으로 pop 하여 진행하였지만, heap이 정렬되는 시간 때문인지 '시간 초과'
   - 그래서 덱을 자료구조로 사용
   - 하지만 델타 탐색을 하면서 상, 하, 좌, 우 의 우선순위를 정해줄 수 없기 때문에, 시간 순서대로 진행한다 하더라도 다른 방향에서 먼저 도착해 있는 경우가 존재했다.
   - 그 경우 진행 시간이 같다면 그대로 직진해 멀리 진행할 수 있도록 조건문 설정이 중요했다.


4. [(골3) 백준 2206 벽 부수고 이동하기](https://www.acmicpc.net/problem/2206)
   - 1이 지나갈 수 없는 벽으로 설정되어, 맨 위 좌측(1 ,1) 에서 맨 아래 우측(N, M)까지의 최단거리를 구하는 문제
   - 조건: 1이된 벽을 '단 하나' 부수고 이동할 수 있음
   - 벽을 부술 수 있는 횟수가 있음에도 벽을 부수고 빠르게 먼저 도착했던 경우가 발생해 2차원 visited 배열로는 구분할 수 없었음
   - 3차원 배열을 이용해 제 3축을 2개로 설정해 벽을 부수고 이동한 경우와 벽을 부수지 않고 이동한 경우로 나누어 visited 처리함

5. [SWEA 22683 나무 베기](https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AZIyCYJ6p30DFAQP)
   - T가 지나갈 수 없는 나무로 설정되어, X 에서 Y까지의 최단거리를 구하는 문제
   - 조건: 나무를 부수고 이동할 수 있는 '횟수 K'가 주어짐
   - 위 4번 문제 처럼 3차원 배열을 이동해 제 3축을 K+1 개로 설정하여 visited 처리한 문제
   - deque로 진행할 경우 cost 순서대로 진행이 안 되고 Y에 도착하더라도 종료되지 않고 모든 heapq를 진행하기 때문에  
     heapq로 하여금 cost 순서대로 진행하여 도착하면 바로 break하도록 설정함
     