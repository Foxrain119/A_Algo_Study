def check(sub):
    counts = 0
    for w in words:
        for l in range(26):
            if w[l] and not sub[l]:
                break
            if l == 25:
                counts += 1
    return counts


def combi(now, count):
    global result, c, can
    if count == n:
        h = check(subset)
        if result < h:
            result = h
        return
    for i in range(now, c):
        if cnt[can[i]]:
            subset[can[i]] = 1
            combi(i + 1, count + 1)
            subset[can[i]] = 0


N, K = map(int, input().split())
n = K - 5  # 가르칠 수 있는 개수
alpha = {'a', 'n', 't', 'i', 'c'}
words = []  # 체킹된 각 단어들
cnt = [0] * 26  # 가르칠 수 있는 종류 체킹
ans = 0

# 각 단어 입력
for _ in range(N):
    tmp = [0] * 26
    # 중복 제외
    w = set(input()[4:-4])
    # {'a', 'n', 't', 'i', 'c'} 제외한 집합
    wa = w - alpha
    # {'a', 'n', 't', 'i', 'c'} 로 읽을 수 있음
    if not len(wa):
        ans += 1
        continue
    # words, cnt 체킹
    for i in wa:
        a = ord(i) - 97
        if a > 26:
            break
        cnt[a] = 1
        tmp[a] = 1
    else:
        words.append(tmp)

# 가르칠 수 있는 글자 종류
can = []
for i in range(26):
    if cnt[i]:
        can.append(i)

c = len(can)
result = 0
subset = [0] * 26
if K < 5:
    print(0)

elif n >= c:
    print(N)
else:
    combi(0, 0)
    print(ans + result)
