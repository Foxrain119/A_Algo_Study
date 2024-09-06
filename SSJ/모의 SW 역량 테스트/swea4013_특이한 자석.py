# import sys
# sys.stdin = open('4013.txt')

from collections import deque # 뭔가 회전한다 -> deque.rotate를 활용하자

t = int(input())

for tc in range(1, t + 1):
    k = int(input())
    wheel = [deque(list(map(int, input().split()))) for _ in range(4)]

    answer = 0

    for _ in range(k):
        num, rot = map(int, input().split())
        num -= 1
        can_rotate = [0] * 4
        
        can_rotate[num] = rot # 무조건 처음 톱니바퀴는 회전한다...

        for i in range(num, 0, -1): # 좌측을 확인
            if wheel[i][6] != wheel[i - 1][2]:
                can_rotate[i - 1] = -can_rotate[i]

        for j in range(num, 3): # 우측을 확인
            if wheel[j][2] != wheel[j + 1][6]:
                can_rotate[j + 1] = -can_rotate[j]

        for l in range(4): # 규칙에 맞게 돌려준다.
            wheel[l].rotate(can_rotate[l])

    answer = wheel[0][0] * 1 + wheel[1][0] * 2 + wheel[2][0] * 4 + wheel[3][0] * 8
    print(f'#{tc} {answer}')