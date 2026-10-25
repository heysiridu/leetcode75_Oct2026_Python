# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

# 如何一次遍历? 使用两个pointers
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        # 如何创建一个空node        
        dum = ListNode(-1)
        dum.next = head

        x = self.findOne(dum, n + 1)
        
        x.next = x.next.next
        return dum.next

    # ListNode | None的含义是，如果 return 的数字是None，是可以被允许的
    def findOne(self, head: ListNode, k : int) -> ListNode | None:
        p1 = head
        # 如何遍历rank(k)?
        for _ in range(k):
            p1 = p1.next

        p2 = head
        while p1:
            p2 = p2.next
            # add the next one
            p1 = p1.next
        
        return p2
