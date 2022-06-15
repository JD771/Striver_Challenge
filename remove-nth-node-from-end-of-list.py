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
