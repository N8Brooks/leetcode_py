from typing import Optional

from definitions.list_node import ListNode


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    previous_node = None
    current_node = head
    while current_node:
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node
    return previous_node
