"""
 @author: huang
 @date: 2024-03-27
 @File: LinkedList.py
 @Description: 
"""


class ListNode:
    """
    节点
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    """
    链表
    """
    def __init__(self):
        self.head = None

    def append(self, val):
        """
        给链表添加新节点（尾部）
        :param val:
        :type val:
        :return:
        :rtype:
        """
        if not self.head:
            # 若为空链表，直接初始化设置头部节点
            self.head = ListNode(val)
        else:
            # 若为非空链表，在最后一个节点链上新节点
            current = self.head
            while current.next:
                # 一直找最后一个节点
                current = current.next
            current.next = ListNode(val)

    def print_self(self):
        """
        展示链表中所有节点的数据
        :return:
        :rtype:
        """
        current = self.head
        while current:
            print(current.val, end=' ')
            current = current.next
        print()


# 使用
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.print_self()  # 输出: 1 2 3
