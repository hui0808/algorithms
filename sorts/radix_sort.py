# 基数排序(Radix Sort) / 桶排序(Bucket Sort)
# 稳定性：稳定
# 时间复杂度，bad：O(d(n+r))；good：O(d(n+rd))，average：O(d(n+r))
# 空间复杂度: O(rd+n)
# d代表最大值的位数，n为个数，r为基数

def radix_sort(array: list) -> list:
    array = array.copy()

    RADIX = 10
    placement = 1

    # get the maximum number
    max_digit = max(array)

    while placement < max_digit:
        # declare and initialize buckets
        buckets = [list() for _ in range(RADIX)]

        # split array between lists
        for i in array:
            tmp = int((i / placement) % RADIX)
            buckets[tmp].append(i)

        # empty lists into array array
        a = 0
        for b in range(RADIX):
            buck = buckets[b]
            for i in buck:
                array[a] = i
                a += 1

        # move to next
        placement *= RADIX

    return array


def test_radix_sort():
    from utils import cachelist
    a = [4, 3, 2, 1]
    a = radix_sort(cachelist(a))
    print(a)


if __name__ == '__main__':
    test_radix_sort()
