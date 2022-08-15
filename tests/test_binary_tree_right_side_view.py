from definitions.tree_node import TreeNode
from problems.binary_tree_right_side_view import right_side_view


def test_example_1():
    assert right_side_view(TreeNode.from_vals([1, 2, 3, None, 5, None, 4])) == [1, 3, 4]


def test_example_2():
    assert right_side_view(TreeNode.from_vals([1, None, 3])) == [1, 3]


def test_example_3():
    assert not right_side_view(TreeNode.from_vals([]))


def test_one_two():
    assert right_side_view(TreeNode.from_vals([1, 2])) == [1, 2]


def test_one_to_four():
    assert right_side_view(TreeNode.from_vals([1, 2, 3, 4])) == [1, 3, 4]
