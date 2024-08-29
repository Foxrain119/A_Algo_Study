import sys
input = sys.stdin.readline
# sys.setrecursionlimit(2500)

def check(): # dfs함수 내에서 배운 k개의 알파벳을 토대로 연산
    cnt1 = 0
    for word in words:
        for wo in word:
            if not alpha[ord(wo) - 97]:
                break
        else:
            cnt1 += 1
    return cnt1

def dfs(start, key): # start 인자를 고려하니 시간복잡도가 해결되었다. 근데 이 방법이 맞는 것일까
    global cnt2

    if key == (k - 5):
        cnt2 = max(cnt2, check())
        return
    
    for i in range(start, 26):
        if not alpha[i]:
            alpha[i] = 1
            dfs(i + 1, key + 1)
            alpha[i] = 0

n, k = map(int, input().split())
words = [input().rstrip() for _ in range(n)]
alpha = [0] * 26
cnt2 = 0

for x in ['a', 'n', 't', 'i', 'c']: # 기본으로 알아야 하는 알파벳들
    alpha[ord(x) - 97] = 1

if k < 5:
    print(0)
elif k == 26:
    print(n)
else:
    dfs(0, 0)
    print(cnt2)