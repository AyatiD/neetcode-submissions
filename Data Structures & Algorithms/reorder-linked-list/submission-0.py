# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #checking for 0 & 1 element
        if not head or not head.next:
            return #this means breaking the function completely & getting out

        #finding the middle element of slow & fast at the end
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        #splitting the list into 2 halves
        second=slow.next
        first=head
        slow.next=None#separating the first half

        #Now reversing the second half
        prev=None
        curr=second
        while curr:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
        second=prev#the very last element which be becomes the first element of the reversed array

        while second:
            #saving the nodes before breaking & joining them alternate
            first_next=first.next
            second_next=second.next

            #connecting first to second node & then 4th to 3rd node in this phase
            first.next=second
            second.next=first_next

            first=first_next
            second=second_next
