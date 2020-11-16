class BinTree:
    def __init__(self):
        self.__root = None
        self.__depth = 0

    @property
    def depth(self):
        return self.__depth

    @property
    def root(self):
        return self.__root

    @root.setter
    def root(self, data):
        self.root = data

    def __iter__(self):
        return self

    def __next__(self):
        pass

    def insert_node(self, data: "BinTreeNode"):
        y = None
        x = self.root
        while x is not None:
            y = x
            if data.key < x.key:
                x = x.left
            else:
                x = x.right

        data.parent = y
        if y is None:
            self.root = data
        elif data.key < y.key:
            y.left = BinTreeNode(data)
        else:
            y.right = BinTreeNode(data)

    def tree_max(self):
        pass


class BinTreeNode:
    def __init__(self, value, parent=None, left=None, right=None):
        self.__value = value
        self.__left = left
        self.__right = right

    @property
    def left(self):
        return self.__left

    @property
    def right(self):
        return self.__right


if __name__ == "__main__":
    tree = BinTree()
    tree.insert_node(BinTreeNode(6))
    tree.insert_node(BinTreeNode(5))