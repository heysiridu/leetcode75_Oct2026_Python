# 141. Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/description/


# two points not sure: 
# not sure where to place the slow as 0, fast as 1. or slow as 0 fast as 0
# not sure shall slow and fast equal and then jump, or slow != fast then jump

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        while fast and fast.next:
            # slow = fast.next
            slow = slow.next
            # fast = slow.next
            fast = fast.next.next

            # if fast.val == slow.val:
            # if slow = fast:
            if slow == fast:
                return True
        
        # return false
        return False
