def find_parent(x):
    if x != gate[x]:
        gate[x] = find_parent(gate[x])
    return gate[x]

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a > b:
        gate[b] = a
    else:
        gate[a] = b

G = int(input()) # gate
P = int(input()) # airplane
gate = [-1] * (G+1)
ans = 0
for i in range(1, P+1):
    target = find_parent(int(input()))
    if not target: break
    union(target - 1, target)
    ans += 1

print(ans)