def find_parent(x):
    if x != city[x]:
        city[x] = find_parent(city[x])
    return city[x]

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:               # 더 적은 수를 루트노드로 지정
        city[b] = a
    else: city[a] = b

N = int(input())
M = int(input())
city = list(range(N+1))
arr = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            union(i+1, j+1)

plan = list(map(int, input().split()))
ans = 'YES'
for i in range(M-1):
    if city[plan[i]] != city[plan[i+1]]: # 루트노드가 다를경우, 비연결
        ans = 'NO'
        break
print(ans)