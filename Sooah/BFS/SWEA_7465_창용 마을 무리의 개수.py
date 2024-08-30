from collections import deque
 
T = int(input())
for tc in range(1, T+1):
    ans = 0
    N, M = map(int, input().split())
    relation = [[] for _ in range((N*(N-1)//2+1))]    # 연결
    for _ in range(M):
        p1, p2 = map(int, input().split())
        relation[p1].append(p2)
        relation[p2].append(p1)
 
    use_num = [0 for _ in range((N*(N-1)//2+1))]      # 무리에 들어갔는지 유무 확인
    if M != 0:                                        # 관계가 있다면, 무리확인
        for i in range(1, N+1):
            if not use_num[i]:     # 이전에 방문 안했다면, 무리 + 1
                ans += 1
                use_num[i] = 1
 
                s = deque([i])
                while s:
                    p = s.popleft()
                    for j in range(len(relation[p])):
                        if use_num[relation[p][j]]: continue
                        use_num[relation[p][j]] = 1
                        s.append(relation[p][j])
    else:                                             # 관계가 없다면, 사람 수 반환
        ans = N
    print(f'#{tc} {ans}')