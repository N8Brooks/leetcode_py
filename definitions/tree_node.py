from __future__ import annotations

from itertools import chain
from typing import List, Optional


class TreeNode:
    """Definition for a binary tree node"""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def from_vals(vals: List[Optional[int]]) -> Optional[TreeNode]:
        """`TreeNode` root with the given `vals` given row by row left to right"""
        nodes = {i: TreeNode(val) for i, val in enumerate(vals) if val is not None}
        for i, node in nodes.items():
            node.left = nodes.get(2 * i + 1, None)
            node.right = nodes.get(2 * i + 2, None)
        return nodes[0] if nodes else None

    def to_vals(self) -> List[int]:
        """Returns the nodes given in row order traversal from `self`"""
        result: List[int] = []
        nodes = (self,)
        while any(nodes):
            result.extend(node.val if node else None for node in nodes)
            temp = ((node.left, node.right) if node else (None, None) for node in nodes)
            nodes = tuple(chain.from_iterable(temp))  # type: ignore
        while result and result[-1] is None:
            del result[-1]
        return result

    def find(self, val: int) -> Optional[TreeNode]:
        """Finds a node with the given `val` if one exists as an ancestor of `self`"""
        stack = [self]
        while stack:
            node = stack.pop()
            if node.val == val:
                return node
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return None
