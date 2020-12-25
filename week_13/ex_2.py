from collections.abc import Iterator
import pickle


class BinTreeIterator(Iterator):
    def __init__(self, tree, pointer):
        self._tree = tree
        self._pointer = pointer
        self._prev_pointer = pointer - 1

    def __next__(self):
        if self._pointer > tree.tree_storage.__len__():
            raise StopIteration()

        self._prev_pointer = self._pointer - 1
        self._pointer += 1
        return tree.tree_storage[self._prev_pointer].key


class BinTree:
    __slots__ = ["__root", "__tree_storage", "__size", "__cur"]

    def __init__(self):
        self.__root = None
        self.__tree_storage = list()
        self.__size = 0
        self.__cur = None

    @property
    def root(self):
        return self.__root

    @root.setter
    def root(self, data):
        self.__root = data

    @property
    def tree_storage(self):
        return self.__tree_storage

    def __iter__(self):
        self.__cur = self.root
        return BinTreeIterator(self, 0)

    def insert_node(self, value: int) -> None:
        x = self.root
        y = None
        while x is not None:
            y = x
            if value < x.key:
                x = x.left
            else:
                x = x.right

        new_node = BinTreeNode(value)
        self.tree_storage.append(new_node)
        self.__size += 1

        if y is None:
            self.root = new_node
        elif y.key > value:
            y.left = new_node
            new_node.parent = y
        else:
            y.right = new_node
            new_node.parent = y

    def tree_max(self):
        x = self.root
        while x.right is not None:
            x = x.right
        return x.key

    def tree_min(self):
        x = self.root
        while x.left is not None:
            x = x.left
        return x.key

    def print_tree(self, x):
        if x is not None and x.key is not None:
            self.print_tree(x.left)
            print(f"//{x.key}\\" + "\\")
            self.print_tree(x.right)

    def clean_tree(self):
        self.__root = None
        self.__tree_storage.clear()
        self.__size = 0
        self.__cur = None

    def dumps_tree(self):
        return pickle.dumps(self)

    def exit_tree(self):
        del self
        print("unalterable process of deleting...")


class BinTreeNode:
    def __init__(self, key, left=None, right=None, parent=None):
        self.__key = key
        self.__left = left
        self.__right = right
        self.__parent = parent

    def __hash__(self):
        return id(self)

    @property
    def left(self):
        return self.__left

    @property
    def right(self):
        return self.__right

    @left.setter
    def left(self, value):
        self.__left = value

    @right.setter
    def right(self, value):
        self.__right = value

    @property
    def key(self):
        return self.__key

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        self.__parent = value


if __name__ == "__main__":
    tree = BinTree()

    tree.insert_node(4)
    tree.insert_node(5)
    tree.insert_node(23)
    tree.insert_node(2)
    tree.insert_node(2)
    tree.insert_node(100)

    serialized_tree = tree.dumps_tree()
    deserialized_tree = pickle.loads(serialized_tree)
    print('\nsuccessfully serialized and deserialized\n')

    for ind, i in enumerate(deserialized_tree):
        print(f"step {ind}: {i}")

    for t in [tree, deserialized_tree]:
        t.exit_tree()
