# 希尔排序(Shell's Sort)
# 稳定性：不稳定
# 时间复杂度，bad：O(n^2)；good：O(n)，average：O(n^(1.3~2))
# 空间复杂度: O(1)

def shell_sort(array: list) -> list:
    length = len(array)
    array = array.copy()
    gap = length // 2
    while gap > 0:
        for i in range(gap, length):
            while i >= gap and array[i] < array[i - gap]:
                array[i], array[i - gap] = array[i - gap], array[i]
                i -= gap
                print('out: ', array)
        gap //= 2
    return array


def test_shell_sort():
    from utils import cachelist
    a = [4, 3, 2, 1]
    a = shell_sort(cachelist(a))
    print(a)


if __name__ == '__main__':
    test_shell_sort()
