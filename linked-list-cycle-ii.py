# Approach 1
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hsh = collections.defaultdict(ListNode)
        while head:
            if head in hsh:
                return head
            hsh[head]= True
            head = head.next
        return None

# Time: O(n)
# Space: O(n)

#Approach 2
def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        entry = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast== slow:
                while entry!= slow:
                    entry = entry.next
                    slow = slow.next
                return entry
        return None
      
# Time: O(n)
# Space: O(1)
