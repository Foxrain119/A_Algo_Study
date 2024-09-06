# defaultdict에 대해 알아보자
# 딕셔너리를 만드는 dict클래스의 서브클래스이다.
# 작동 방식은 거의 동일한데, defaultdict()는 인자로 주어진 객체(default-factory)의 기본 값을 딕셔너리의 초깃값으로 지정할 수 있다.
# 말 그대로 처음 키를 지정할 때 값을 주지 않으면 해당 키에 대한 값을 디폴트 값으로 지정하겠다는 뜻이다.
# defaultdict(int) -> 이 때 딕셔너리의 특정 key의 값은 항상 0으로 자동 초기화된다.
# defaultdict(list) -> 이 때 딕셔너리의 특정 key의 값은 항상 []으로 자동 초기화된다.

from collections import deque, defaultdict
 
t = int(input())
 
for tc in range(1, t + 1):
    n, m, k = map(int, input().split()) # 셀의 개수, 격리 시간, 군집의 개수
    dq = deque()
    for _ in range(k):
        r, c, num, move = map(int, input().split())
        dq.append([r, c, num, move])
 
    drow = [0, -1, 1, 0, 0]
    dcol = [0, 0, 0, -1, 1]
 
    while m > 0:
        # 각 단계(m)에서 군집들의 이동 후 상태를 저장하는 딕셔너리 -> (행 인덱스, 열 인덱스)를 키 값으로 가진다.
        # 겹치는 경우 처리 후 value들을 deque에 넣어준다.
        # 특정 좌표를 키 값으로 가지는 빈 리스트를 만들어야 하는데, dict의 경우 미리 키 값에 해당하는 빈 리스트를 지정해주지 않으면 아래 코드 실행이 복잡해진다.
        temp_dict = defaultdict(list) 
        for _ in range(len(dq)): # 각 단계에서 모든 군집이 이동을 해보자 -> len(dq)에 주목
            # 여기서 x가 아니라 변수명으로 리스트 원소 값을 저장해주었으면 좀 더 명시적이었을 것이다.
            x = dq.popleft()
            nr = x[0] + drow[x[3]]
            nc = x[1] + dcol[x[3]]
             
            if nr == 0 or nr == (n - 1) or nc == 0 or nc == (n - 1): # 여기선 겹칠 수 없음(경계선)
                x[2] //= 2
                if x[3] in [1, 3]:
                    x[3] += 1
                else:
                    x[3] -= 1
                 
                if x[2] > 0: # 군집이 소멸된 경우에는 temp_dict에 넣어주지 않는다.
                    temp_dict[(nr, nc)].append([nr, nc, x[2], x[3]])
            else:
                temp_dict[(nr, nc)].append([nr, nc, x[2], x[3]])
 
        for key, value in temp_dict.items():
            if len(value) > 1: # 특정 좌표에서 군집이 겹칠 때(두 개 이상일 때!)
                total_num = sum([x[2] for x in value]) # 군집들의 개수 합
                max_num = max([x[2] for x in value]) # 군집 개수들 중 최대값
                new_move = [x[3] for x in value if x[2] == max_num][0] # 다음 이동 방향 지정
                dq.append([key[0], key[1], total_num, new_move]) 
            else:
                dq.append(value[0])
 
        m -= 1
     
    answer = sum([v[2] for v in dq])
    print(f'#{tc} {answer}')