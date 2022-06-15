# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy= head
        count = 0
        while dummy:
            count +=1
            dummy = dummy.next
        
        if n<0 or n>count:
            return None
        if n==count:
            head = head.next
            
        curr = head
        N = count-n
        new_count = 0
        while curr:
            if new_count == N-1:
                curr.next = curr.next.next
                break
            curr = curr.next
            new_count +=1
        return head

 # This solution will take the time complexity of O(n+n) i.e., O(2n) & the space complexity of O(1).
# There is an optimized solution using two pointer approach.

def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast, slow = head, head
        for i in range(n):
            fast = fast.next
        
        if not fast:
            return head.next
            
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head

# This solution will take time O(n) & space O(1).
