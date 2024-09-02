# import sys
# sys.stdin = open('1244.txt', 'r')

t = int(input())

for tc in range(1, t + 1):
    temp, cnt = input().split()
    cards = list(map(int, list(temp)))
    cnt = int(cnt)
    len_cards = len(cards)
    idx = 0
    temp_idx = 0

    while cnt > 0:
        # 해당 인덱스 기준 이후 값 중 최대 값을 찾아준다!
        max_val = -1
        for i in range(idx + 1, len_cards):
            if cards[i] > max_val:
                max_val = cards[i]
                temp_idx = i

        # 해당 인덱스 이후 값 중 최대 값이 여러개인 경우를 처리해주자...
        temp_lst = []; cnt2 = 0
        for j in range(idx + 1, len_cards):
            if cards[j] == max_val:
                temp_lst.append(j)
            if cards[j] <= cards[idx]:
                cnt2 += 1

        # 인덱스가 len_cards - 2에 도달했다 -> 그 이전까지는 최대값 조건 만족 -> 이후에 중복된 숫자가 있다면 중복된 숫자끼리 변경해주면 된다!!!
        if idx == len_cards - 2:
            num = [0] * 10
            for ca in cards:
                num[ca] += 1

            flag = False

            for nu in num:
                if nu >= 2:
                    flag = True # 중복 값이 있다면 True
                    break
            
            if cnt % 2 != 0: 
                if flag:
                    break
                else:
                    cards[idx], cards[idx + 1] = cards[idx + 1], cards[idx]
                    cnt -= 1
            else:
                break
        else:
            if cards[idx] >= max_val:
                idx += 1
            else:
                if cnt2 >= len(temp_lst):
                    temp_idx = temp_lst[0]
                else:
                    temp_idx = temp_lst[len(temp_lst) - 1 - cnt2]
                temp = cards[idx]
                cards[idx] = max_val
                cards[temp_idx] = temp

                cnt -= 1
                idx += 1

    answer = ''.join(map(str, cards))
    print(f'#{tc} {answer}')