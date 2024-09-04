def backtrack(cnt):
    global max_sum
    price = int("".join(arr))

    if (cnt, price) in visited:
        return
    visited.add((cnt, price))

    if cnt == time:
        max_sum = max(max_sum, price)
        return

    for i in range(n-1):
        for j in range(i+1, n):
            arr[i], arr[j] = arr[j], arr[i]
            backtrack(cnt + 1)
            arr[i], arr[j] = arr[j], arr[i]

t = int(input())

for tc in range(1, t+1):
    arr, time = input().strip().split()
    n = len(arr)
    arr, time = list(arr), int(time)
    max_sum = 0
    visited = set()
    backtrack(0)
    print(f"#{tc} {max_sum}")