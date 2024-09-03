from collections import deque
 
t = int(input())
 
for tc in range(1, t + 1):
    n, k = map(int, input().split())
    length = n // 4
    dq = deque(input())
    numbers = []
 
    for _ in range(n - 1):
        for j in range(0, n, length):
            temp = 0 # 10진수로 변환 후 담아 줄 변수
            for l in range(length):
                if dq[j + l].isdigit():
                    temp += int(dq[j + l]) * (16 ** (length - 1 - l))
                else:
                    if dq[j + l] == 'A':
                        temp += 10 * 16 ** (length - 1 - l)
                    elif dq[j + l] == 'B':
                        temp += 11 * 16 ** (length - 1 - l)
                    elif dq[j + l] == 'C':
                        temp += 12 * 16 ** (length - 1 - l)
                    elif dq[j + l] == 'D':
                        temp += 13 * 16 ** (length - 1 - l)
                    elif dq[j + l] == 'E':
                        temp += 14 * 16 ** (length - 1 - l)
                    elif dq[j + l] == 'F':
                        temp += 15 * 16 ** (length - 1 - l)
            numbers.append(temp)
        dq.rotate(1) # deque rotate를 활용하자
     
    numbers = sorted(list(set(numbers)), reverse=True) # 중복 값 제거, 내림차순 정렬
    print(f'#{tc} {numbers[k - 1]}')