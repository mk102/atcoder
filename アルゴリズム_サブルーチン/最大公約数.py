def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)

def main():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))

    ans = 0
    for i in x:
        ans = GCD(ans, abs(X - i))
    print(ans)

    return 0


if __name__ == '__main__':
    main()