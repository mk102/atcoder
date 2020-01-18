import itertools
import numpy as np
import math


def binary_search(A, B, X):
    low = 0
    high = 10 ** 9

    while abs(low - high) != 1:
        # print(low, high)
        mid = (high + low) // 2
        price = A * mid + B * len(str(mid))
        if price <= X:
            low = mid
        else:
            high = mid
    return high, low


def main():
    A, B, X = map(int, input().split())
    high, low = binary_search(A, B, X)
    if (A * high + B * len(str(high))) <= X:
        print(high)
    else:
        print(low)
    return 0


if __name__ == '__main__':
    main()
import itertools
import numpy as np
import math


def binary_search(A, B, X):
    low = 0
    high = 10 ** 9

    while abs(low - high) != 1:
        # print(low, high)
        mid = (high + low) // 2
        price = A * mid + B * len(str(mid))
        if price <= X:
            low = mid
        else:
            high = mid
    return high, low


def main():
    A, B, X = map(int, input().split())
    high, low = binary_search(A, B, X)
    if (A * high + B * len(str(high))) <= X:
        print(high)
    else:
        print(low)
    return 0


if __name__ == '__main__':
    main()