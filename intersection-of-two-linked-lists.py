# Approach 1

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a = headA
        b = headB
        count1 = 0
        while a:
            count1 +=1
            a = a.next
        count2 = 0
        while b:
            count2 +=1
            b = b.next
        
        a = headA
        b = headB
        if count1> count2:
            diff = count1 - count2
            while diff:
                diff-=1
                a = a.next
        elif count2> count1:
            diff = count2- count1
            while diff:
                diff-=1
                b = b.next
        while count1> 0:
            if a == b:
                return a
            a = a.next
            b = b.next
            count1 -=1
        return
      
     # Time: O(M+N), worst case: O(2M)
    # Space: O(1)
    
# Approach 2
class Solution:
    def changeSign(self, head: ListNode):
        while ( head ):
            head.val *= -1
            head = head.next
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        self.changeSign(headA)
        
        while ( headB ):
            if headB.val < 0:break
            headB = headB.next
        
        self.changeSign(headA)
        return headB
      
# Time Complexity: O(3N) or O(N)
# Space Complexity: O(1)

# Approach 3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None
        a = headA
        b = headB
        
        while a!= b:
            a = headB if a is None else a.next
            b = headA if b is None else b.next
        return b
      
# Time complexity: O(2M) (Worst case)
# Space Complexity: O(1)
