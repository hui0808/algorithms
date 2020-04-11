# 用py模拟链表的行为，py本身是不需要自己去实现链表的，因为list就是很好链表

class Node(object):
    # 双向循环链表
    def __init__(self, item=None):
        self.item = item
        self.prev = self
        self.next = self

    def __repr__(self):
        return f'Node({self.item!r})'

class List(object):
    def __init__(self):
        self.count = 0
        self.head = Node('head')

    def __add(self, prev, new, next):
        next.prev = new
        prev.next = new
        new.prev = prev
        new.next = next

    def __pop(self, prev, next):
        prev.next = next
        next.prev = prev

    def add(self, item, index=None):
        head = self.head
        new = Node(item)
        if index is None:
            self.__add(head, new, head.next)
            self.count += 1
        elif isinstance(index, int) and index >= 0:
            n = head
            for _ in range(index):
                n = n.prev
                if n == head:
                    raise IndexError
            self.__add(n.prev, new, n)
            self.count += 1
        else:
            raise TypeError

    def pop(self, index=None):
        head = self.head
        if index is None:
            r = head.next
            self.__pop(r.prev, r.next)
            r.next = r.prev = r
            self.count -= 1
            return r.item

        elif isinstance(index, int) and index >= 0:
            n = head
            for _ in range(index + 1):
                n = n.prev
                if n == head:
                    raise IndexError
            self.__pop(n.prev, n.next)
            n.next = n.prev = n
            self.count -= 1
            return n.item
        else:
            raise TypeError

    def length(self):
        return self.count

    def __iter__(self):
        head = self.head
        n = head.prev
        while n != head:
            yield n.item
            n = n.prev

    def __str__(self):
        return f'List[{", ".join(str(i) for i in self)}]'


if __name__ == '__main__':
    head = List()
    head.add(2)
    head.add(3)
    head.add(4)
    head.pop(2)
    print(head)

