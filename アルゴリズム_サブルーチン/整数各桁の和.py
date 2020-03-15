def findSumOfDigits(n):
    sum = 0
    while n > 0:
        sum += n%10
        n //= 10
    return sum

def main():
    N = int(input())
    print(findSumOfDigits(N))

    return 0


if __name__ == '__main__':
    main()