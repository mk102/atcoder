import math
import collections
import numpy as np

def main():
    S = input()
    ans = 0

    for i in range(len(S)):
        ori_chr = S[i:]
        srt_chr = sorted(ori_chr)

        pre_c = "0"
        numer = math.factorial(len(S) - 1 - i)
        for j, srt_c in enumerate(srt_chr):

            if srt_c == ori_chr[0]:
                break

            if pre_c == srt_c:
                continue

            pre_c = srt_c
            item = collections.Counter(srt_chr)
            item[srt_c] -= 1

            denom = np.prod(list(map(math.factorial, list(item.values()))))

            ans += (numer / denom)
    print(int(ans) + 1)
    return 0

if __name__ == '__main__':
    main()