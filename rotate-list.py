# Approach 1
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None: return head
        temp = head
        length = 0
        while temp:
            length +=1
            temp = temp.next
        k = k% length
        while k:
            dummy = head
            while dummy.next.next:
                dummy = dummy.next
            last = dummy.next
            dummy.next = None
            last.next = head
            head = last
            k-=1
        return head
      
# Time: O(k*n)
# Space: O(1)

# Approach 2
def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None: return head
        temp = head
        length = 1
        while temp.next:
            temp = temp.next
            length +=1
        temp.next = head
        k = length- (k%length)
        while k:
            temp = temp.next
            k-=1
        head = temp.next
        temp.next = None
        return head
      
# Time: O(n)
# Space: O(1)
