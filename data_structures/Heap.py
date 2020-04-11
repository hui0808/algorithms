from data_structures.List import List


class Heap(List):
    def __str__(self):
        return f'Heap[{", ".join(str(i) for i in self)}]'

    def push(self, item):
        super().add(item)

    def pop(self, index=0):
        return super().pop(index)

if __name__ == '__main__':
    s = Heap()
    s.push(1)
    s.push(2)
    while s.length() != 0:
        print(s.pop())