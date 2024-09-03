T = int(input())
for tc in range(1, T+1):
    num, change = map(int, input().split()) # num: 숫자판 / change: 교환횟수
    num = list(map(int, str(num)))

    compare = [0] * len(num)                # 바뀐 수 저장
    cnt_same = 0                            # 동일한 수 유무 확인
    for i in range(len(num)-1):             # 맨 앞 수부터 검사
        m = num[i]                          # 바꿀 왼쪽 대상 저장
        idx = i                             # 바꿀 오른쪽 대상 인덱스
        for j in range(len(num)-1, i, -1):  # 바꿀 오른쪽 대상은 뒤에서부터 검사 (가장 큰 수 만들기 위해)
            if m < num[j]:                  # 바꿀 왼쪽 대상보다 크면, 오른쪽 대상 갱신
                m = num[j]
                idx = j
            if num[i] == num[j]:            # 바꿀 왼족 대상과 오른쪽 대상이 있다면, 동일한 수 체크
                cnt_same += 1
        if idx == i:                        # 바꿀 대상이 없으면 pass
            continue

        num[i], num[idx] = num[idx], num[i] # 바꾸기
        change -= 1

        compare[idx] = num[idx]             # 바뀐 수 저장
        if i != 0 and before == num[i]:     # 지금 바꾼 수와 이전에 바꾼 수가 같다면, ex) 32888 -> 88823, 88832 둘다 가능하므로 88832로 바꿔주어야 함
            for k in range(idx+1, len(num)):
                if compare[k] > compare[idx]: # 이전에 바꾼 값이 더 크다면, 교환
                    compare[k], compare[idx] = compare[idx], compare[k]
                    num[k], num[idx] = num[idx], num[k]

        if change == 0 or (change and i == len(num) - 1): # 바꿀 기회가 남았는데, 문자열 끝까지 검사한 경우
            break
        before = num[i]

    if cnt_same == 0 and change % 2: # 동일한 값이 없는 경우, 남은 횟수가 홀수일 때
        num[-1], num[-2] = num[-2], num[-1]
        change = 0

    print(f'#{tc}', ''.join(map(str, [x for x in num])))