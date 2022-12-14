from definitions.tree_node import TreeNode
from problems.binary_tree_level_order_traversal import level_order


def test_example_1() -> None:
    root = TreeNode.from_vals([3, 9, 20, None, None, 15, 7])
    assert level_order(root) == [[3], [9, 20], [15, 7]]


def test_example_2() -> None:
    root = TreeNode.from_vals([1])
    assert level_order(root) == [[1]]


def test_example_3() -> None:
    assert not level_order(None)
