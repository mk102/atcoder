def main():
    N = int(input())
    i = 2
    while i ** 2 <= N:
        if N % i == 0:
            print("NO")
            return 0
        i += 1
    print("YES")

    return 0


if __name__ == '__main__':
    main()