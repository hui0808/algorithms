# 堆排序(Heap sort)
# 稳定性：不稳定
# 时间复杂度，bad：O(n*log2(n))；good：O(n*log2(n))，average：O(n*log2(n))
# 空间复杂度: O(1)

def heap_sort(array: list) -> list:
    length = len(array)
    array = array.copy()

    # 从最后一个非叶子节点向上迭代，构造一个大顶堆
    for i in range(length // 2 - 1, -1, -1):
        heapify(array, i, length)
    # 将堆顶元素与末尾元素进行交换，使末尾元素最大。然后继续调整堆
    for i in range(length - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        print('out:', array)
        # 堆的大小恰好不包括末尾元素，使其只对末尾元素以上调整
        heapify(array, 0, i)

    return array


def heapify(array, index, heap_size):
    # 从index位置开始，构造一个顶堆
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    if left_index < heap_size and array[left_index] > array[largest]:
        largest = left_index
    if right_index < heap_size and array[right_index] > array[largest]:
        largest = right_index
    if largest != index:
        array[largest], array[index] = array[index], array[largest]
        print('out:', array)
        # 若发生交换，则要从更换的位置更新这个顶堆
        heapify(array, largest, heap_size)


def test_heap_sort():
    from utils import cachelist
    a = [4, 3, 2, 1]
    a = heap_sort(cachelist(a))
    print(a)


if __name__ == '__main__':
    test_heap_sort()
