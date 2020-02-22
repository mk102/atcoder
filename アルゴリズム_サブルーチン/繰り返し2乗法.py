import math
def main():
    m = (10 ** 9) + 7
    n, a, b = map(int, input().split())

    a_k = math.factorial(a)
    b_k = math.factorial(b)

    # フェルマーの小定理
    a_k = pow(a_k, m - 2, m)
    b_k = pow(b_k, m - 2, m)

    n_a = 1
    for i in range(n-a+1, n+1):
        n_a = (n_a * i) % m

    n_b = 1
    for i in range(n-b+1, n+1):
        n_b = (n_b * i) % m

    n_C_a = a_k * n_a
    n_C_b = b_k * n_b

    n_C_a = n_C_a % m
    n_C_b = n_C_b % m

    p = pow(2, n, m)

    print((p - n_C_a - n_C_b - 1)%m)
    return 0

if __name__ == '__main__':
    main()