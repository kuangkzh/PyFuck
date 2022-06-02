from collections import defaultdict
import itertools
import multiprocessing
import tqdm


class DictSearcher:
    def __init__(self, charset, length, min_key):
        self.charset = charset
        self.length = length
        self.min_key = min_key

    def search(self, left):
        left = ''.join(left)
        d = defaultdict(lambda: "b" * 100)
        for j in range(1, self.length):
            for b in itertools.product(self.charset, repeat=j):
                if b.count("0") == j:
                    continue
                s = f"0x{left}%0x{''.join(b)}"
                res = eval(s)
                if res < 128:
                    d[res] = min(s, d[res], key=self.min_key)
        return dict(d)


def count_extra_char(s):
    return sum(s.count(c) for c in "2468bdf"), len(s)


def search(charset, left_len, right_len):
    ans = defaultdict(lambda: "b"*100)
    for i in range(1, left_len):
        searcher = DictSearcher(charset, right_len, count_extra_char)
        updates = [*pool.imap(searcher.search, tqdm.tqdm([*itertools.product(charset, repeat=i)]))]
        for update in updates:
            ans.update({k: min(ans[k], update[k], key=count_extra_char) for k in update})
        if len(ans) == 128 and all(count_extra_char(ans[k])[0] <= k % 2 for k in ans):
            break
    return ans


if __name__ == "__main__":
    pool = multiprocessing.Pool(8)
    d_ce0 = search("0ce", 6, 4)
    d_bce0 = search("0bce", 10, 4)
    d_cde0 = search("0cde", 10, 4)
    d_even = search("02468bcdef", 10, 4)

    print(len(d_ce0), dict(d_ce0))
    print(len(d_bce0), sum(count_extra_char(d_bce0[k])[0] for k in d_bce0), dict(d_bce0))
    print(len(d_cde0), sum(count_extra_char(d_cde0[k])[0] for k in d_cde0), dict(d_cde0))
    print(len(d_even), sum(count_extra_char(d_even[k])[0] for k in d_even), dict(d_even))
