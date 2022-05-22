# ==============================================================================
# * Implement an algorithm to find the nth to last element of a singly linked list
# ==============================================================================


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def append(self, val=0):
        dup = self
        while dup.next:
            dup = dup.next
        dup.next = ListNode(val)


def nth_last_element(head: ListNode, n: int):
    dup = head
    slow = dup
    fast = dup
    for _ in range(n):
        if fast:
            fast = fast.next
        else:
            break

    while fast:
        slow = slow.next
        fast = fast.next

    return slow
    # 1 -> 2 -> 3 -> 4 -> 5 -> 6


head = ListNode(1)
head.append(2)
head.append(3)
head.append(4)
head.append(5)
head.append(6)

if nth_last_node := nth_last_element(head, 9):
    print(nth_last_node.val)
else:
    print(nth_last_node)
