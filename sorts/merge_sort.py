# 归并排序(Merge Sort)
# 稳定性：稳定
# 时间复杂度，bad：O(n*log2(n))；good：O(n*log2(n))，average：O(n*log2(n))
# 空间复杂度: O(n)

def merge_sort(array: list) -> list:

    def merge(left, right):
        result = []
        while left and right:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        return result + left + right

    length = len(array)
    mid = length // 2
    if length <= 1:
        return array
    return merge(merge_sort(array[:mid]), merge_sort(array[mid:]))


def test_merge_sort():
    from utils import cachelist
    a = [4, 3, 2, 1]
    a = merge_sort(cachelist(a))
    print(a)


if __name__ == '__main__':
    test_merge_sort()