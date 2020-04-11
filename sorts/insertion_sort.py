# 直接插入排序(Insertion sort)
# 稳定性：稳定
# 时间复杂度，bad：O(n^2)；good：O(n)，average：O(n^2)
# 空间复杂度: O(1)

def insertion_sort(array: list) -> list:
    length = len(array)
    array = array.copy()
    for i in range(1, length):
        while i > 0 and array[i] < array[i - 1]:
            # 将array[i]与前一个将array[i-1]比较
            array[i], array[i - 1] = array[i - 1], array[i]
            i -= 1
            print('out:', array)
    return array


def test_insertion_sort():
    from utils import cachelist
    a = [4, 3, 2, 1]
    a = insertion_sort(cachelist(a))
    print(a)


if __name__ == '__main__':
    test_insertion_sort()
