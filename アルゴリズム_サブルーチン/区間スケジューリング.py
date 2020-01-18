def main():
    N = int(input())
    robo = []

    for _ in range(N):
        x, l = map(int, input().split())
        robo.append((x-l, x+l))

    robo = sorted(robo, key=lambda x:x[1])

    ans = 0
    max = -10**9

    for r in robo:
        if r[0] >= max:
            ans += 1
            max = r[1]
    print(ans)
    return 0

if __name__ == '__main__':
    main()
