def calc_digit(n):
    digit = 0
    while n > 0:
        digit += 1
        n //= 10
    return digit

def main():
    N = int(input())
    i = 1
    digit = []
    ans = 10
    while i ** 2 <= N:
        if N % i == 0:
            tmp = calc_digit(N // i)
            if ans > tmp:
                ans = tmp
        i += 1
    print(ans)

    return 0


if __name__ == '__main__':
    main()