N, M, Q = map(int, input().split())
query = []
for _ in range(Q):
    query.append(tuple(map(int, input().split())))

ans = []

# 単調増加考慮
def dfs(l):
    if len(l) == N:
        tmp = 0
        for q in query:
            if (l[q[1]-1] - l[q[0]-1]) == q[2]:
                tmp += q[3]
        ans.append(tmp)
        return
    prev = l[-1] if len(l) > 0 else 1
    for v in range(prev, M+1):
        l.append(v)
        dfs(l)
        l.pop()


dfs([])
print(max(ans))