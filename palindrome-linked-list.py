# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(head: Optional[ListNode])-> Optional[ListNode]:
            prev = None
            curr = head
            
            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev
        
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        slow.next = reverse(slow.next)
        slow = slow.next
        
        while slow:
            if head.val != slow.val:
                return False
            head = head.next
            slow = slow.next
        return True
      
# Time: O(n)
# Space: O(1)
