from typing import Optional, Iterable, Union


class Node(object):
    def __init__(self, item: Union[int, float]):
        self.right = None
        self.left = None
        self.item = item

    def __str__(self):
        return f'Node({self.item})'


class Tree(object):
    PRE = 1  # 前序
    IN = 2  # 中序
    POST = 3  # 后序

    def __init__(self, items: Iterable[Union[int, float]] = None):
        self.count = 0
        self.root = None
        self.order = self.PRE
        if items is not None:
            for i in items:
                self.add(i)

    def add(self, item: Union[int, float]):
        return self.__add(Node(item), self.root)

    def delete(self, item: Union[int, float]):
        return self.__delete(item, self.root, self.root)

    def find(self, item: Union[int, float]):
        return self.__find(item, self.root)

    def iter(self, order=None):
        # 遍历这棵树
        # order: 遍历方法
        def _iter(root, order):
            # 递归写法
            if root is not None:
                if order == self.PRE:
                    yield root.item
                yield from _iter(root.right, order)
                if order == self.IN:
                    yield root.item
                yield from _iter(root.left, order)
                if order == self.POST:
                    yield root.item

        yield from _iter(self.root, order or self.order)

    def __find(self, item, root):
        if root is None:
            return False
        elif self.toleft(item, root.item):
            if root.left is None:
                return False
            else:
                self.__find(item, root.left)
        elif self.toleft(root.item, item):
            if root.right is None:
                return False
            else:
                self.__find(item, root.right)
        else:
            return True

    def __add(self, item: Node, root):
        if self.root is None:
            self.root = item
        elif self.toleft(item.item, root.item):
            if root.left is None:
                root.left = item
                self.count += 1
            else:
                self.__add(item, root.left)
        elif self.toleft(root.item, item.item):
            if root.right is None:
                root.right = item
                self.count += 1
            else:
                self.__add(item, root.right)
        else:
            raise Exception('二叉排序树不允许添加相同元素')

    def __delete(self, item, root, prev):
        if root is None:
            return False
        if self.toleft(item, root.item):
            if root.left is None:
                return False
            else:
                self.__delete(item, root.left, root)
        elif self.toleft(root.item, item):
            if root.right is None:
                return None
            else:
                self.__delete(item, root.right, root)
        else:
            if self.toleft(item, prev.item):
                prev.left = self.__consNode(root)
            elif self.toleft(prev.item, item):
                prev.right = self.__consNode(root)
            else:
                self.root = self.__consNode(root)
            self.count -= 1
            return True


    def __consNode(self, node):
        # 将一个节点的两个子节点合成一棵树
        if node.left is None or node.right is None:
            return node.left or node.right
        else:
            self.__add(node.left, node.right)
            return node.right

    def toleft(self, item, root):
        return item > root


if __name__ == '__main__':
    t = Tree([1, 7, 2, 9, 6])
    t.delete(1)
    for i in t.iter(t.IN): # 从小到大打印
        print(i)
