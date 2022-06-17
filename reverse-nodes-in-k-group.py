# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k==1 or head is None:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        temp = head
        prev = dummy
        next_node = dummy
        count= 0
        while temp:
            count +=1
            temp = temp.next
            
        while count>= k:
            temp = prev.next
            next_node = temp.next
            for i in range(1,k):
                temp.next = next_node.next
                next_node.next = prev.next
                prev.next = next_node
                next_node = temp.next
            prev = temp
            count-=k
        return dummy.next      

# Time: O(N)
# Space: O(1)
