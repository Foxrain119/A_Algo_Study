# import sys
# sys.stdin = open('1494.txt', 'r')

def factorial(x):
    if x == 1:
        return 1
    return x * factorial(x - 1)

def combi_counts(num, take): # 조합의 개수를 반환하는 함수
    return factorial(num) // (factorial(num - take) * factorial(take))
    

def backtracking(idx, key):
    global answer, finish

    if finish == combi_counts(n, n // 2) // 2: # 절반만 탐색해도 된다. 조합의 특성 -> 4C2일 때, (1, 2), (1, 3), (1, 4)만 알면 나머지는 반대 값만 남음(2, 3) (2, 4) (3, 4)
        return

    if key == n // 2:
        finish += 1
        for cs in range(2): # 두 번의 경우를 뒤집뒤집
            temp_sum_x = 0
            temp_sum_y = 0
            if cs == 0:
                for i in range(n):
                    if i in ten_lst:
                        temp_sum_x -= worms[i][0]
                        temp_sum_y -= worms[i][1]
                    else:
                        temp_sum_x += worms[i][0]
                        temp_sum_y += worms[i][1]
                if temp_sum_x ** 2 + temp_sum_y ** 2 < answer:
                    answer = temp_sum_x ** 2 + temp_sum_y ** 2
            else:
                for i in range(n):
                    if i in ten_lst:
                        temp_sum_x += worms[i][0]
                        temp_sum_y += worms[i][1]
                    else:
                        temp_sum_x -= worms[i][0]
                        temp_sum_y -= worms[i][1]
                if temp_sum_x ** 2 + temp_sum_y ** 2 < answer:
                    answer = temp_sum_x ** 2 + temp_sum_y ** 2
        return
    
    for i in range(idx, n):
        ten_lst.append(i)
        backtracking(i + 1, key + 1)
        ten_lst.pop()

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    worms = [0] * n
    for i in range(n):
        x, y = map(int, input().split())
        worms[i] = (x, y)
    ten_lst = []
    answer = float('Inf') # 시간복잡도 4,645ms
    # answer = 2 * 2000000 ** 2 # 시간복잡도 4,766ms
    finish = 0

    backtracking(0, 0)

    print(f'#{tc} {answer}')