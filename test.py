def main():
    N, M = map(int, input().split())
    S = []
    for _ in range(M):
        S.append(tuple(map(int, input().split())))

    for i in range(0, 10**N):
        k = str(i)
        count = 0
        if len(k) < N:
            continue
        for s, c in S:
            if k[s-1] == str(c):
                count += 1
        if count == M:
            print(i)
            return 0
    print(-1)

    return 0


if __name__ == '__main__':
    main()