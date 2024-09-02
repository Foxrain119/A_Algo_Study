from itertools import permutations
 
def backtracking(permutation, depth):
    global result, left, right
 
    if depth == n:
        result += 1
        return
     
    if left > avgchu: # 왼쪽 저울에 총 질량의 반 이상이 올라가 있다면 -> 근데 표현이 애매해서 고쳐야 할 것 같음
        result += 2 ** (n - depth)
        return
    elif left < right + permutation[depth]: # 현재 값을 더했을 때 오른 저울 값이 커진다면(조건에 위배)
        left += permutation[depth] # 왼쪽 저울에 더해주고
        backtracking(permutation, depth + 1) # 계속 진행
        left -= permutation[depth]
    else:
        left += permutation[depth]
        backtracking(permutation, depth + 1)
        left -= permutation[depth]
        right += permutation[depth]
        backtracking(permutation, depth + 1)
        right -= permutation[depth]
 
t = int(input())
 
for tc in range(1, t + 1):
    n = int(input())
    chu = list(map(int, input().split()))
    avgchu = sum(chu) // 2 # 재귀 함수나 반복문에서 상수처럼 사용되는 값은 변수로 지정해주자!
    permu = list(permutations(chu, n)) # 순열을 구해준다.
 
    result = 0
    for perm in permu:
        left = 0
        right = 0
        backtracking(perm, 0)
     
    print(f'#{tc} {result}')