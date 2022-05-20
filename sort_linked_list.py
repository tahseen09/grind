# ==============================================================================
# * Sort List [Leetcode #148]
# ! Time Complexity - O(nlogn)
# ==============================================================================


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge(head1: Optional[ListNode], head2: Optional[ListNode]):
    if not head1:
        return head2
    if not head2:
        return head1

    head1 = head1
    head2 = head2
    res = None
    head = None  # ! To point to the first element in resultant list
    while head1 and head2:
        if head1.val <= head2.val:
            new_node = ListNode(head1.val)
            head1 = head1.next
        else:
            new_node = ListNode(head2.val)
            head2 = head2.next
        if not res:
            res = new_node
            head = res
        else:
            res.next = new_node
            res = res.next

    if head1:
        while head1:
            res.next = head1
            res = res.next
            head1 = head1.next
    elif head2:
        while head2:
            res.next = head2
            res = res.next
            head2 = head2.next
    return head


def sortList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head
    slow = head
    fast = head
    if not head.next.next:
        # ! Handling only elements in linked list, if not handled -> it can go into infinite execution
        slow = head
        fast = head.next
    else:
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

    head2 = slow.next
    slow.next = None
    res1 = sortList(head)
    res2 = sortList(head2)
    return merge(res1, res2)


def Print(head):
    head_x = head
    while head_x:
        print(head_x.val, end=" -> ")
        head_x = head_x.next


n1 = ListNode(100)
n1.next = ListNode(1)
n1.next.next = ListNode(-1)
n1.next.next.next = ListNode(90)

Print(sortList(n1))
