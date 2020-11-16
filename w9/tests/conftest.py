import pytest
from scripts.ex_1 import BinTree
from scripts.ex_2 import TextLoader


@pytest.fixture()
def prepared_tree_for_minimax():
    tree_1 = BinTree()
    tree_2 = BinTree()
    tree_3 = BinTree()

    tree_1.insert_node(4)
    tree_1.insert_node(5)
    tree_1.insert_node(23)
    tree_1.insert_node(2)  # min
    tree_1.insert_node(2)
    tree_1.insert_node(100)  # max

    tree_2.insert_node(4)
    tree_2.insert_node(5)  # max
    tree_2.insert_node(2)
    tree_2.insert_node(3)
    tree_2.insert_node(5)
    tree_2.insert_node(1)  # min

    tree_3.insert_node(0)
    tree_3.insert_node(0)
    tree_3.insert_node(0)
    tree_3.insert_node(0)
    tree_3.insert_node(-1)  # min
    tree_3.insert_node(10)  # max

    return [
        [tree_1.tree_min(), tree_2.tree_min(), tree_3.tree_min()],
        [tree_1.tree_max(), tree_2.tree_max(), tree_3.tree_max()]
    ]


@pytest.fixture()
def prepared_tree_for_iter():
    tree_1 = BinTree()
    tree_2 = BinTree()
    tree_3 = BinTree()

    tree_1.insert_node(4)
    tree_1.insert_node(5)
    tree_1.insert_node(23)
    tree_1.insert_node(2)  # min
    tree_1.insert_node(2)
    tree_1.insert_node(100)  # max

    tree_2.insert_node(4)
    tree_2.insert_node(5)  # max
    tree_2.insert_node(2)
    tree_2.insert_node(3)
    tree_2.insert_node(5)
    tree_2.insert_node(1)  # min

    tree_3.insert_node(0)
    tree_3.insert_node(0)
    tree_3.insert_node(0)
    tree_3.insert_node(0)
    tree_3.insert_node(-1)  # min
    tree_3.insert_node(10)  # max

    return [
        list(tree_1),
        list(tree_2),
        list(tree_3)
    ]


# =========================================

path_list = [
    "/Users/vlasenckov/MIPT/git_project/MIPT_py_3_term/w9/sample.zip",
    "/Users/vlasenckov/MIPT/git_project/MIPT_py_3_term/w9/one_more_sample.zip"
]


@pytest.fixture(name="len_of_folder")
def check_len():
    global path_list
    text_1 = TextLoader(path_list[0])
    text_2 = TextLoader(path_list[1])

    return [
        len(text_1),
        len(text_2)
    ]
