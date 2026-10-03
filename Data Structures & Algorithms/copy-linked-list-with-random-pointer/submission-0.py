"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copies={}
        curr=head

        while curr:
            copies[curr]=Node(curr.val)
            curr=curr.next
        
        curr=head

        #now connecting the random & base pointers to the value 
        while curr:
            copy=copies[curr]
            copy.next=copies.get(curr.next)
            copy.random=copies.get(curr.random)

            curr=curr.next

        return copies.get(head)