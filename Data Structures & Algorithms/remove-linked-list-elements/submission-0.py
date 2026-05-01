# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        #recursive method
        if not head:
            return None
        #recursively call function on head.next to process list
        head.next = self.removeElements(head.next, val)

        #if head.val = val, return head.next to skip current node
        return head if head.val != val else head.next