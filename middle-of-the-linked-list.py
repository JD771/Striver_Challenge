# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Brute Force
        '''count = 0
        curr = head
        while curr:
            curr = curr.next
            count += 1
        new_count = (count//2)
        while new_count:
            head = head.next
            new_count-=1
        return head
        '''
        
        # Fast & Slow Pointer
        slow, fast = head, head
        while fast!= None and fast.next!= None:
            slow = slow.next
            fast = fast.next.next
        return slow
