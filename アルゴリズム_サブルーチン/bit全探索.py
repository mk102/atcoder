def main():
    N = int(input())

    data = []
    for i in range(N):
        A = int(input())
        items = []
        for j in range(A):
            x, y = map(int, input().split())
            items.append((x-1, y))
        data.append(items)

    ans = 0

    for i in range(1, 2**N):
        tmp = 0
        flag = True
        for j in range(N):
            if (i>>j)&1 == 1:
                tmp += 1
                for d in data[j]:
                    if (i>>d[0])&1 != d[1]:
                        flag = False
        if (flag) & (tmp > ans):
            ans = tmp
    print(ans)

    return 0
if __name__ == '__main__':
    main()