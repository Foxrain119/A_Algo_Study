'''
문제링크 : https://www.acmicpc.net/problem/1062

<input>
3 6
antarctica
antahellotica
antacartica

<output>
2
'''

def back(idx, learn_cnt):
    global ans, alpha
    if learn_cnt == K-5:
        my_word = 0
        for j in range(N):
            if alpha & word_li[j] == word_li[j]: # 배운 단어면
                my_word += 1
        ans = max(ans, my_word)
        return

    for i in range(idx, 26):
        if alpha & (1<<i) == 0: # 안 배운 알파벳이면
            alpha |= (1<<i)     # 배우기 / alpha[i] = 1
            back(i, learn_cnt+1) # 배운 알파벳 수 +1
            alpha &= ~(1<<i)    # 안배우기 / alpha[i] = 0

N, K = map(int, input().split())  # N: 문장개수 / K: 배울 수 있는 알파벳 수
if K - 5 < 0:   # 남극 기본언어(5개)도 못 배우면, 읽을 수 있는 문장 없음
    print(0) 
elif K == 26:
    print(N)    # 모든 알파벳을 배우면, 모든 문장 읽을 수 있음
else:
    alpha = 0                             # 배운 단어 (비트연산위함(26자). 00 0000 0000 0000 0000 0000 0000)
    base_li = ['a', 'n', 't', 'i', 'c']   # 남극 기본 언어
    for base in base_li:
        alpha |= 1 << ord(base)-ord('a')  # 남극언어 배움

    word_li = [0 for _ in range(N)] # 배워야 하는 문장(비트연산용)
    for i in range(N):
        tmp = input()[4:-4]         # 남극 기본 언어 제외 (anta, tica)
        for w in tmp:
            word_li[i] |= (1 << ord(w)-ord('a'))

    ans = 0     # 읽을 수 있는 최대 문장
    back(0, 0)
    print(ans)