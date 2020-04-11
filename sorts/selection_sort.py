# 选择排序(Selection sort)
# 稳定性：不稳定
# 时间复杂度，bad：O(n^2)；good：O(n^2)，average：O(n^2)
# 空间复杂度: O(1)

def selection_sort(array: list) -> list:
    length = len(array)
    array = array.copy()
    for i in range(length - 1):
        small = i
        for j in range(i + 1, length):
            if array[small] > array[j]:
                small = j
        if small != i:
            array[i], array[small] = array[small], array[i]
            print('out:', array)
    return array


def test_selection_sort():
    from utils import cachelist
    a = [4, 3, 2, 1]
    a = selection_sort(cachelist(a))
    print(a)


if __name__ == '__main__':
    test_selection_sort()
