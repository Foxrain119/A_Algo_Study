# 문제의 조건대로 구현해보는 연습을 하자. 내가 원래 알던 방식으로 바라보려고 하면 중간 사고 과정에서 꼬인다.
# 원소의 x, y좌표가 주어졌다고 생각해보자. x값이 변화한다는 것은 열의 인덱스 값이 이동한다는 것이다. y값이 변화한다는 것은 행의 인덱스 값이 이동한다는 것이다.
# 델타 리스트를 생성할 때 일반적으로 내가 아는 방식으로 설정해주면 안되는 것이다!
# 다양한 원소가 동시에 행동한다 -> deque를 활용하자
# 좌표 값의 위치가 음수이다 -> 모든 좌표 값에 동일한 값을 더해 0이상의 값으로 만들어주자
# 스치면 소멸한다 -> 예를 들어, 1.5초에 만나면 소멸한다. -> 각 좌표값과, grid 길이를 2배로 늘려주자.
# 그 이외에는 미생물 문제와 비슷함..

from collections import deque, defaultdict

t = int(input())

for tc in range(1, t + 1):
    n = int(input()) # 원자 개수
    dxy = [(0, 1), (0, -1), (-1, 0), (1, 0)] # 상, 하, 좌, 우

    dq = deque()
    for _ in range(n):
        x, y, dir, energy = map(int, input().split()) # x 좌표, y 좌표!!!
        dq.append(((x + 1000) * 2, (y + 1000) * 2, dir, energy)) # 음수인 좌표 값을 0이상으로 만들어주고 스치면 충돌을 해결하기 위해 0.5를 곱해준다.

    answer = 0
    while dq:
        temp_dict = defaultdict(list)
        for _ in range(len(dq)):
            px, py, pdir, penergy = dq.popleft()
            npx = px + dxy[pdir][0]
            npy = py + dxy[pdir][1]

            if npx < 0 or npx > 4000 or npy < 0 or npy > 4000: # 인덱스 밖으로 나가면 소멸
                continue

            temp_dict[(npx, npy)].append((npx, npy, pdir, penergy))

        for key, value in temp_dict.items():
            if len(value) > 1: # 충돌하면 에너지를 방출하고 소멸
                for tp in range(len(value)):
                    answer += value[tp][3]
            else:
                dq.append(value[0])
             
    print(f'#{tc} {answer}')