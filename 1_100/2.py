# Definition for singly-linked list.
#2. 两数相加
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # 设置头指针 head主要是输出 now为当前指针
        head = now = ListNode()
        isAdd = 0
        while True:
            # l1为空则为FALSE
            # 如果当前l1或l2为空则给x或y赋默认值0
            x = l1.val if l1  else 0
            y = l2.val if l2  else 0
            # 相加
            total = x+y+isAdd
            # 判断是否进位
            isAdd = 0 if total < 10 else 1
            # 设置下一个值为当前值%10
            now.next = ListNode(total%10)
            # l1 为空则为TRUE即l1
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            # 全部为空进位为0则跳出循环
            if l1 is None and l2 is None and isAdd == 0:
                break
            now = now.next
        return head.next
Solution().addTwoNumbers(None,None)