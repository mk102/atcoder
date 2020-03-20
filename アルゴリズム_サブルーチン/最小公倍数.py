def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)

def LCM(a, b):
    return a // GCD(a, b) * b

def main():
    A, B = map(int, input().split())
    print(LCM(A, B))

    return 0


if __name__ == '__main__':
    main()