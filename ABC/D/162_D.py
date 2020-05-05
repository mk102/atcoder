import math
import collections

def main():
    N = int(input())
    S = input()

    c = collections.Counter(S)
    c = c['R'] * c['G'] * c['B']

    count = 0
    for i in range(N):
        for j in range(i+1, N):
            k = 2*j-i
            if k < N:
                if (S[i] != S[j]) and (S[j] != S[k]) and (S[i] != S[k]):
                    count += 1

    print(c - count)
    return 0

if __name__ == '__main__':
    main()