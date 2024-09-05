'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?contestProbId=AZGhzGZq18oDFAXd&solveclubId=AZCz7ha6bv8DFAVs&problemBoxTitle=999.+A%ED%98%95%EC%9D%84+%EB%94%B0%EB%B3%B4%EC%9E%90&problemBoxCnt=4&probBoxId=AZGhIDtKx30DFAXd

=== 재귀와 메모이제이션으로 백트래킹을 구현하는 문제 ===

처음엔 순열로 접근하여 각 순열마다 점수를 측정했는데
N이 10일 때 10! 이면 3628800이므로 점수 측정의 복잡도가 약 30이 넘어가면 당연히 터짐

그 다음엔 순열을 구한 상태에서 점수를 구할 때, 하나씩 지울 때 마다 dict 에 넣고 그 값이 있으면 끊어줬는데
애초에 순열을 구해서 진행하는게 순열에서 끊어줄 수 없으니 잘못된 것이었음

재귀로 하나씩 터트려가면서 들어가면서 현재 상태의 max 값을 dict 에 메모이제이션하며 백트래킹을 구현

재귀 너무 어렵다...
'''
def recur(tpl):
    if tpl in memo:
        return memo[tpl]

    max_score = 0
    for i in range(1, len(tpl) - 1):
        if tpl[i - 1] != 0 and tpl[i + 1] != 0:
            tmp = tpl[i - 1] * tpl[i + 1]
        elif tpl[i - 1] == 0 and tpl[i + 1] != 0:
            tmp = tpl[i + 1]
        elif tpl[i - 1] != 0 and tpl[i + 1] == 0:
            tmp = tpl[i - 1]
        else:
            tmp = tpl[i]

        remain = recur(tpl[:i] + tpl[i + 1:])
        total = tmp + remain
        max_score = max(max_score, total)

    memo[tpl] = max_score
    return max_score


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = (0,) + tuple(map(int, input().split())) + (0,)

    memo = {(0, 0): 0}
    result = recur(arr)

    print(f'#{tc} {result}')