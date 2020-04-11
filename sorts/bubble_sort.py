# 冒泡排序(Bubble Sort)
# 稳定性：稳定
# 时间复杂度，bad：O(n^2)；good：O(n)，average：O(n^2)
# 空间复杂度: O(1)

def bubble_sort(array: list) -> list:
    length = len(array)
    array = array.copy()
    swap_flag = False
    for i in range(length - 1):
        for j in range(length - 1 - i):
            if array[j] > array[j + 1]:
                swap_flag = True
                array[j], array[j + 1] = array[j + 1], array[j]
                print('out:', '\t' * i, array)
        if swap_flag is False:
            break
    return array

def test_bubble_sort():
    from utils import cachelist
    a = [4, 3, 2, 1]
    a = bubble_sort(cachelist(a))
    print(a)

if __name__ == '__main__':
    test_bubble_sort()