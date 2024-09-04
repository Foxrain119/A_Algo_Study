'''
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWAe7XSKfUUDFAUw

순열 + 부분집합
백트래킹

어떻게 끊어줘서 실행시간을 단축시키냐가 중요한 문제
'''
def permute(cnt, l_cnt, r_cnt):
    global result, a_sum
    # 종료 조건
    if cnt == N:
        result += 1
        return
    # === 잘라주는 조건 === ( 좌측 무게가 전체 추 무게의 절반 이상이면 더 볼 필요 없음, 뒤는 모든 경우의 수가 가능)
    if l_cnt > a_sum:
        n = N - cnt
        result += 2 ** n * dp[n]  # 2의 n제곱 * n!
        return

    # 순열
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            permute(cnt + 1, l_cnt + arr[i], r_cnt)
            if arr[i] + r_cnt <= l_cnt:
                permute(cnt + 1, l_cnt, r_cnt + arr[i])
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    a_sum = sum(arr) // 2  # 무게추 총 합의 절반
    visited = [0] * N
    result = 0

    # 팩토리얼 저장
    dp = [0, 1]
    j = 1
    while j < 10:
        dp.append(dp[j] * (j+1))
        j += 1

    permute(0, 0, 0)
    print(f'#{tc} {result}')
