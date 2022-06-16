# Approach 1-> Using hashing
def hasCycle(self, head: Optional[ListNode]) -> bool:
        hsh = set()
        while head:
            if head in hsh:
                return True
            hsh.add(head)
            head = head.next
        return False
      
 # Time: O(N)
# Space: O(N)-> since we are creating a hashmap & storing the values

# Approach 2-> Using slow & fast pointers (Also called Floyd's tortoise and hare algorithm)
def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast== slow:
                return True
# Time: O(N)
# Space: O(1)

# Approach 3-> Using a single pointer, marking the already visited nodes as None
def hasCycle(self, head: Optional[ListNode]) -> bool:
        while head:
            if head.val:
                head.val = None
            else:
                return True
            head = head.next
        return False
      
# Time: O(N)
# Space: O(1)
