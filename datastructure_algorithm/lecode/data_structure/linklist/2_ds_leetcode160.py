# 定义单链表节点
class ListNode:
    def __init__(self, x):
        self.value = x
        self.next = None


def intersection_of_two_linklists(headA: ListNode, headB: ListNode) -> ListNode:
    if not headA or not headB:
        return None

    p1 = headA
    p2 = headB
    while p1 != p2:
        p1 = headB if not p1 else p1.next
        p2 = headA if not p2 else p2.next
    return p1
