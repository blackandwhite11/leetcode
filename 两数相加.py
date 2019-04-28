# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
# 示例：
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
# 请注意，我们使用哑结点来简化代码。如果没有哑结点，则必须编写额外的条件语句来初始化表头的值。


class ListNode(object):
    # define link-list
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 定义一个哑节点，简化代码，无需再添加判断条件
        lis = ListNode(0)
        cur = lis
        carry = 0
        while l1 or l2:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            sum = n1 + n2 + carry
            carry = sum//10
            cur.next = ListNode(sum%10)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry != 0:
            cur.next = ListNode(carry)
        return lis.next


def create_link(lis):
    link_start = ListNode(0)
    head = link_start
    for i in lis:
        head.next = ListNode(i)
        head = head.next
    return link_start.next


if __name__ == "__main__":
    li_1 = [2, 4, 3]
    li_2 = [5, 6, 4]
    link_1 = create_link(li_1)
    link_2 = create_link(li_2)
    solu = Solution()
    cur = solu.addTwoNumbers(link_1, link_2)
    while cur:
        print(cur.val)
        cur = cur.next




