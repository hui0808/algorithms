from data_structures.List import List


class Stack(List):
    def __str__(self):
        return f'Stack[{", ".join(str(i) for i in self)}]'

    def push(self, item):
        super().add(item)

if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    while s.length() != 0:
        print(s.pop())
