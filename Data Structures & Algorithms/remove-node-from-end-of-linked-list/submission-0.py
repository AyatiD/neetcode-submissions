# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        left=dummy
        right=dummy

        #pushing the right node +n of left=head
        for _ in range(n):
                right=right.next

        while right.next:#we gotta stop when right is last element not right=none
            left=left.next
            right=right.next

        #reaching the value where left.next is the one which needs to be skipped/removed
        left.next=left.next.next

        return dummy.next