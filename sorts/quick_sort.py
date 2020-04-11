# 快速排序(Quick Sort)
# 稳定性：不稳定
# 时间复杂度，bad：O(n^2)；good：O(n*log2(n))，average：O(n*log2(n))
# 空间复杂度: O(log2(n))

def quick_sort(array: list) -> list:
    # 挖坑填数法, 空穴法
    def inner_sort(array, left, right):
        if left >= right:
            return
        flag = True  # True从右向左，False从左向右
        pivot = array[left]  # 中心点
        i, j = left, right
        while i < j:
            if flag:
                # 从右向左找一个小于pivot的数
                if array[j] >= pivot:
                    j -= 1
                else:
                    array[i] = array[j]
                    print('out:', array, '右向左', pivot)
                    i += 1
                    flag = False
            else:
                # 从左向右找一个大于pivot的数
                if array[i] <= pivot:
                    i += 1
                else:
                    array[j] = array[i]
                    print('out:', array, '左向右', pivot)
                    j -= 1
                    flag = True
        if i != left:
            array[i] = pivot
            print('out:', array, 'pivot填坑', pivot)
            inner_sort(array, left, i - 1)
        inner_sort(array, i + 1, right)

    length = len(array)
    array = array.copy()
    inner_sort(array, 0, length - 1)
    return array


def test_quick_sort():
    from utils import cachelist
    a = [4, 3, 2, 1]
    a = quick_sort(cachelist(a))
    print(a)


if __name__ == '__main__':
    test_quick_sort()
