def get(l, v, default=0):
    if v < 0:
        return default
    try:
        return l[v]
    except IndexError:
        return default


def create_empty_matrix(example):
    h = len(example)
    w = len(example[0])
    m = [[None] * w for _ in range(h)]
    return m


def mprint(m):
    print(*m, "", sep="\n")


def hflip(m):
    return [r[::-1] for r in m]


def vflip(m):
    return m[::-1]


def miter(m):
    for idx, row in enumerate(m):
        for jdx, h in enumerate(row):
            yield idx, jdx, h


def sliding_max(m):
    #mprint(m)
    mmax = create_empty_matrix(m)
    for idx, jdx, h in miter(m):
        top = get(get(mmax, idx - 1, default=[]), jdx) or 0
        right = get(get(mmax, idx, default=[]), jdx - 1) or  0
        mmax[idx][jdx] = max(min(top, right), h)
    #mprint(mmax)
    #print()
    return mmax


class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """

        top_right = sliding_max(heightMap)
        top_left = hflip(sliding_max(hflip(heightMap)))
        bottom_right = vflip(sliding_max(vflip(heightMap)))
        bottom_left = vflip(hflip(sliding_max(vflip(hflip(heightMap)))))

        #result = create_empty_matrix(heightMap)

        total = 0

        for idx, jdx, h in miter(heightMap):
            tr = top_right[idx][jdx]
            tl = top_left[idx][jdx]
            br = bottom_right[idx][jdx]
            bl = bottom_left[idx][jdx]
            res = min(tr, tl, br, bl)
            total += res - h
            #result[idx][jdx] = res
        #mprint(result)
        return total


if __name__ == '__main__':
    assert Solution().trapRainWater(
        [[1, 1, 1],
         [1, 0, 2],
         [3, 0, 3],
         [1, 1, 1]]
    ) == 2
    assert Solution().trapRainWater(
        [[3, 3, 3, 3, 3],
         [3, 2, 2, 2, 3],
         [3, 2, 1, 2, 3],
         [3, 2, 2, 2, 3],
         [3, 3, 3, 3, 3]]
    ) == 10
