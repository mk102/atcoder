import math
import collections

# 単調増加考慮しない
'''
def dfs(l, M, N):
    if len(l) == M:
        print(l)
        return

    for v in range(N):
        l.append(v)
        dfs(l, M, N)
        l.pop()
'''

# 単調増加考慮
def dfs(l, M, N):
    if len(l) == M:
        print(l)
        return
    prev = l[-1] if len(l) > 0 else 1
    for v in range(prev, N):
        l.append(v)
        dfs(l, M, N)
        l.pop()

def main():
    dfs([], 3, 3)
    return 0

if __name__ == '__main__':
    main()