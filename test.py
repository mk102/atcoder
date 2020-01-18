import bisect

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L = sorted(L)

    ans = 0

    for i in range(N):
        for j in range(i+1, N):
            X = L[i] + L[j]
            l = bisect.bisect_left(L, X, lo=j+1)
            ans += (l-(j+1))
            #print(L[j + 1:l])
    print(ans)
    return 0

if __name__ == '__main__':
    main()
