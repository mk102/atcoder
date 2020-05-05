import math
import collections

def main():
    N = int(input())
    A = list(map(int, input().split()))

    c = collections.Counter(A)
    for i in range(1, N+1):
        print(c[i])

    return 0

if __name__ == '__main__':
    main()